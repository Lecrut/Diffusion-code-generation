import math

def compute_fibonacci(n):
    sqrt5 = math.sqrt(5)
    phi = (1 + sqrt5) / 2
    psi = (1 - sqrt5) / 2
    return round((phi ** n - psi ** n) / sqrt5)

def first_n_fibonacci(n):
    return [compute_fibonacci(i) for i in range(n)]

if __name__ == '__main__':
    results = first_n_fibonacci(80)
    for i, val in enumerate(results):
        print(f"{i}: {val}")