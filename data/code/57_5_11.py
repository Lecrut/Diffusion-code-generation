import math

def fibonacci(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    sqrt5 = math.sqrt(5)
    phi = (1 + sqrt5) / 2
    psi = (1 - sqrt5) / 2
    fn = (phi ** n - psi ** n) / sqrt5
    return round(fn)

if __name__ == '__main__':
    results = [fibonacci(i) for i in range(80)]
    for i, val in enumerate(results):
        print(f"F({i}) = {val}")