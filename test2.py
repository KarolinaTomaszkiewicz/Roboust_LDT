import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert, chirp
import statistics

duration = 1.0
fs = 400.0
samples = int(fs * duration)
# t = np.arange(samples) / fs

# signal = chirp(t, 20.0, t[-1], 100.0)
# signal *= (1.0 + 0.5 * np.sin(2.0*np.pi*3.0*t) )


t = []
signal = []

with open('zestaw1.txt') as f:
    content = f.readlines()


content = [x.strip() for x in content]

for item in content:
    t.append(float(item.split(' ')[0]))
    signal.append(float(item.split(' ')[1]))

print(len(t))
print(signal)

x = statistics.mean(signal)

signal = [item - x for item in signal]



plt.plot(t, signal)
plt.show()

analytic_signal = hilbert(signal)
amplitude_envelope = np.abs(analytic_signal)
instantaneous_phase = np.unwrap(np.angle(analytic_signal))
instantaneous_frequency = (np.diff(instantaneous_phase) /
                           (2.0 * np.pi) * fs)

fig = plt.figure()
ax0 = fig.add_subplot(211)
ax0.plot(t, signal, label='signal')
ax0.plot(t, amplitude_envelope, label='envelope')
ax0.set_xlabel("time in seconds")
ax0.legend()
ax1 = fig.add_subplot(212)
ax1.plot(t[1:], instantaneous_frequency)
ax1.set_xlabel("time in seconds")
ax1.set_ylim(0.0, 120.0)
plt.show()

