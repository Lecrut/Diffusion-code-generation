import math

def factorial_iterative(n):
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    values = [0, 1, 5, 10, 20]
    for val in values:
        computed = factorial_iterative(val)
        expected = math.factorial(val)
        assert computed == expected, f"Mismatch for {val}"
        print(f"factorial_iterative({val}) = {computed}")