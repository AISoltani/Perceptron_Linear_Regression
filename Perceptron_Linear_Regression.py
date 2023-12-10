# I

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Loading dataset from pandas lib

x = pd.read_csv("spambase_X.csv",header=None)
y = pd.read_csv("spambase_y.csv",header=None)
x = np.array(x)
y = np.array(y)
y = np.reshape(y,-1)
print(x)
print(y)
n,d = x.shape
mistake = np.zeros(500)
w = np.zeros(d)
b = 0
iteration=500

for i in range(iteration):
    Mistake = 0
    for j in range(n):
        if (y[j] * (np.dot(w.T,x[j,:]) + b) <= 0):
            w = w + y[j]*x[j,:]
            b = b + y[j]
            Mistake = Mistake + 1   
    mistake[i] = Mistake
    
plt.figure()
plt.plot(range(iteration), mistake)
plt.xlabel('Number of Passes')
plt.ylabel('Number of Mistakes')
plt.show()
