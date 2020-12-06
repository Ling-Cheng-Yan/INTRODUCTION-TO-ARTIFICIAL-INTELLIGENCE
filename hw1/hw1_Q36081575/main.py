from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import math
from functions import func

with open('input.txt', 'r') as f:
    numbers = [lines.rstrip('\n') for lines in f.readlines()]



#--------P1(BF)--------
x = numbers[0].split(',')
y = numbers[1].split(',')
x0 = int(x[0])
x1 = int(x[1])
y0 = int(y[0])
y1 = int(y[1])

lst0 = list()
lst1 = list()

for a in range(x0, x1 +1):
    for b in range(y0, y1+1):
        lst1.append(func(a, b))
        if lst1[-1] <= min(lst1):
            a_x = a
            b_y = b
print('-----P1(BF) Answer-----')
print('P1(BF) result X: ', int(a_x))
print('P1(BF) result Y: ', int(b_y))
print('P1(BF) result Z: ', round(min(lst1), 3))



#--------P2(SA)--------
x = [i/10 for i in range(1000)]
y = [i/10 for i in range(1000)]
z = [0 for i in range(1000)]
for i in range(1000):
    z[i] = func(x[i], y[i])

T = 1000 #initiate temperature
Tmin = 10 #minimum value of terperature
x = np.random.uniform(low=0,high=100)#initiate x
y = np.random.uniform(low=0,high=100)#initiate y
k = 50 #times of internal circulation 
z = 0 #initiate result
t = 0 #time
while T >= Tmin:
    for i in range(k):
        #calculate z
        z = func(x, y)
        #generate a new x in the neighboorhood of x by transform function
        xNew = x + np.random.uniform(low=-0.055,high=0.055) * T
        yNew = y + np.random.uniform(low=-0.055,high=0.055) * T
        if (0 <= xNew and xNew <= 100):
            zNew = func(xNew, yNew)
            if zNew - z < 0:
                x = xNew
                y = yNew
            else:
                #metropolis principle
                p = math.exp(-(zNew - z) / T)
                r = np.random.uniform(low=0,high=1)
                if r < p:
                    x = xNew
                    y = yNew
    t += 1
    T = 1000/(1+t)

print('-----P2(SA) Answer-----')
print('P2(SA) result X: ', int(x))
print('P2(SA) result Y: ', int(y))
print('P2(SA) result Z: ', round(func(x, y), 3))
