def compute_factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == '__main__':
    test_values = [0, 1, 5, 10]
    for value in test_values:
        print(compute_factorial(value))