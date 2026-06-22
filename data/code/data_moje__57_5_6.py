import math

def fibonacci_binet(n):
    sqrt5 = math.sqrt(5)
    phi = (1 + sqrt5) / 2
    psi = (1 - sqrt5) / 2
    fib = (phi ** n - psi ** n) / sqrt5
    return int(round(fib))

if __name__ == '__main__':
    for i in range(80):
        print(fibonacci_binet(i))