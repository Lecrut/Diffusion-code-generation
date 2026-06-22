import math

def compute_fibonacci(n):
    sqrt5 = math.sqrt(5)
    phi = (1 + sqrt5) / 2
    psi = (1 - sqrt5) / 2
    return int(round((phi ** n - psi ** n) / sqrt5))

if __name__ == '__main__':
    for i in range(80):
        print(compute_fibonacci(i))