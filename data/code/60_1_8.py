def compute_factorial(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    result = 1
    current = 1
    while current <= n:
        result *= current
        current += 1
    return result

if __name__ == '__main__':
    test_values = [0, 1, 5, 7, 10]
    for value in test_values:
        print(compute_factorial(value))