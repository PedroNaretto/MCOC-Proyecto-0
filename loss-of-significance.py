# -*- coding: utf-8 -*-
"""
Created on Sun Aug 04 20:50:05 2019

@author: Pedro
"""

import numpy as np
from numpy import *

num32 = np.linspace(0,0.1,10000, dtype = float32)
num64 = np.linspace(0,0.1,10000, dtype = float64)

num32 = np.delete(num32,0)
num64 = np.delete(num64,0)

v32 = []
v64 = []
diff = []
numeros = []

for x in num32:
   
    #Funcion calculada con 32 bits
    val32 = np.float32(((1 -np.cos(x))/np.sin(x)))
    v32.append(val32)
    numeros.append(x)
    if len(v32) == 50:
        break

for x in num64:
   
    #Funcion calculada con 64 bits
    val64 = np.float64(((1 -np.cos(x))/np.sin(x)))
    v64.append(val64)
    if len(v64) == 50:
        break

for i in range(len(v32)-1):
    #Diferencia de exactitud entre calculos con 32 y 64 bits
    diff.append(np.abs((v32[i]-v64[i])/v64[i]))
    
print "Numeros utilizados"
print numeros
print ""
print "Calculos con 32 bits"
print v32
print ""
print "Calculos con 64 bits"
print v64
print ""
print "Error Relativo"
print diff