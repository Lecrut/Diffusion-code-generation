import math

def fibonacci(n):
    if n < 0:
        return 0
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    result = (pow(phi, n) - pow(psi, n)) / math.sqrt(5)
    return round(result)

if __name__ == '__main__':
    for i in range(80):
        print(fibonacci(i))