#!/usr/bin/python3
import sys

##############################################################################
# functions that generate fibonacci numbers
#
# reFib is the classical recursive example
#
# memFib uses memoization to achieve greater efficiency
#
# for larger numbers iteration is best (iterFib)

fibs = {}

def memFib(n=0):
    if n not in fibs:
        fibs[n] = reFib(n-1) + reFib(n-2)

    return fibs[n]


def reFib(n=0):
    if n <= 0: return 0
    elif n <= 2: return 1
    else: return reFib(n-1) + reFib(n-2)


def iterFib(n=0):
    a = 0
    b = 1 
    c = 1
    i = 2
    if n <= 0: return a
    elif n <= 2: return b

    while i < n:
        a = b
        b = c
        c = a + b
        i += 1
    return c

# should return 6765
#print(iterFib(20))
#print(memFib(20))
#print(reFib(20))

# should return 9227465
#print(iterFib(35))
#print(memFib(35))
#print(reFib(35))

# should return 12586269025
#print(iterFib(50))
#print(memFib(50))
#print(reFib(50))

print(iterFib(int(sys.argv[1])))
print(memFib(int(sys.argv[1])))
# commented out recursive form because for values 
# larger than 40 it will seem to run forever
# print(reFib(int(sys.argv[1])))
