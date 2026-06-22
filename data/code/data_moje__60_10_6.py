def calculate_factorial(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    result = 1
    current = 1
    while current <= n:
        result *= current
        current += 1
    return result

if __name__ == '__main__':
    test_values = [0, 1, 5, 10]
    for value in test_values:
        print(calculate_factorial(value))