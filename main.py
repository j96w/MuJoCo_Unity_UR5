from mjremote import mjremote
import time
import math
import numpy

m = mjremote()
print('Connect: ', m.connect())
b = bytearray(3*m.width*m.height)
t0 = time.time()
t1 = time.time()
m.getimage(b)
bb = numpy.frombuffer(b)
print(bb.shape)


print(m.getnqpose())
m.setqpos(numpy.array([0.1, -50 / 180 * math.pi, 61.03 / 180 * math.pi,
               0, 0, 0, # robotic arm
               0, 0, 0, 0,
               0, 0, 0, 0, # two fingers
               -0.62, 0.32, 0, math.cos(math.pi * 0.16), 0, 0, math.sin(math.pi * 0.16),
               -0.72, 0.38, 0, math.cos(math.pi * 0.18), 0, 0, math.sin(math.pi * 0.18),
               -0.835, 0.425, 0, math.cos(math.pi * 0.195), 0, 0, math.sin(math.pi * 0.195),
               -0.935, 0.46, 0, math.cos(math.pi * 0.23), 0, 0, math.sin(math.pi * 0.23)] + [0] * 77))
print('FPS: ', 100/(t1-t0))
m.close()
