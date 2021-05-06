#factorion finding
import math as math

def factorion(a, b):
    factorions = []
    for i in range(a, b):
        if sum(math.factorial(int(d)) for d in str(i)) == i: factorions.append(i)
        
    return factorions

factorion(1,10)
