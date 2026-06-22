def factorial_iterative(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    values = [0, 1, 5, 10, 20]
    for v in values:
        print(factorial_iterative(v))