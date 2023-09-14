import numpy as np

filename = input("Type the full filepath of your csv file: ")
arr = np.loadtxt(filename, dtype=float, delimiter=',')

x = arr[:,0]
x2 = x*x
y = arr[:,1]
one = np.ones(len(x))

mat = np.vstack([one,x,x2]).T
mat_t = mat.T

ls = mat_t.dot(mat)
b = mat_t.dot(y)

param = np.linalg.inv(ls).dot(b)

def p(x):
    return param[0] + param[1]*x + param[2]*x*x

def R(x):
    return p(x)*x

def dR(x):
    return (param[1] + 2*param[2]*x)*x + p(x)

min = x[0]
max = x[len(x)-1]

def false_position(a,b):
    c = (a*dR(b) - b*dR(a)) / (dR(b) - dR(a))
    if abs(dR(c)) < .01:
        return c
    elif dR(a) >= 0 and dR(c) >= 0:
        return false_position(c, b)
    else:
        return false_position(a, c)

price = false_position(min, max)
print(price)
