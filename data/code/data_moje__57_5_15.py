import math

def fibonacci(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    sqrt5 = math.sqrt(5)
    phi = (1 + sqrt5) / 2
    psi = (1 - sqrt5) / 2
    return int((phi ** n - psi ** n) / sqrt5 + 0.5)

def generate_first_80_fibonacci():
    results = []
    for i in range(80):
        results.append(fibonacci(i))
    return results

if __name__ == '__main__':
    fib_80 = generate_first_80_fibonacci()
    for i, val in enumerate(fib_80):
        print(f"F({i}) = {val}")
    print(f"F(79) = {fib_80[79]}")