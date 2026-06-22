import math

def compute_fibonacci(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    sqrt_5 = math.sqrt(5)
    phi = (1 + sqrt_5) / 2
    psi = (1 - sqrt_5) / 2
    fib_n = (phi ** n - psi ** n) / sqrt_5
    return int(round(fib_n))

def generate_first_80_fibonacci():
    results = []
    for i in range(80):
        results.append(compute_fibonacci(i))
    return results

if __name__ == '__main__':
    fib_numbers = generate_first_80_fibonacci()
    print(fib_numbers)