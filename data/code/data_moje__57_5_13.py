import math

def compute_fibonacci_binet(n: int) -> int:
    if n < 0:
        raise ValueError("Index must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    sqrt_5 = math.sqrt(5)
    phi = (1 + sqrt_5) / 2
    value = (phi ** (n + 1)) / sqrt_5
    return int(round(value))

if __name__ == '__main__':
    results = []
    for i in range(80):
        results.append(compute_fibonacci_binet(i))
    for i, val in enumerate(results):
        print(f"F({i}) = {val}")