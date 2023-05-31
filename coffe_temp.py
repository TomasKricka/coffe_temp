import numpy as np
import matplotlib.pyplot as plt
import time
import serial
import struct
import codecs
import csv
import pandas as pd
import sys


s = serial.Serial( port="COM4", baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

i = 0

with open('tempp.csv', 'w',newline='\n' , encoding='utf-8') as f:
    header = [ 'time', 'temp']
    writer = csv.writer(f, delimiter=';')
    writer.writerow(header)
    f.close()

while(1):
    
    
    i = i + 1
    temp_b = float(s.readline())
    print(temp_b)

    plt.plot(i, temp_b, 'bo')
    #time.sleep(1)
    plt.pause(0.005)
    plt.grid()
    
    with open('tempp.csv', 'a',newline='\n' , encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow([i, temp_b])
        f.close()
plt.show()
s.close()
