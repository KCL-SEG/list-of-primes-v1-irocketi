"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
import math

def checkPrime(x):
    if x == 2 or x == 3:
        return True
    for i in range(2, math.ceil(x/2)+1):
        if x%i == 0:
            return False
    return True

def primes(number_of_primes):
    list = []
    x = 1
    while len(list) <= number_of_primes:
        isPrime = checkPrime(x)
        if isPrime:
            list.append(x)
        x += 1
    return list

primes(10)
