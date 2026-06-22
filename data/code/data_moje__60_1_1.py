def factorial(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative")
    if n == 0:
        return 1
    result = 1
    counter = 2
    while counter <= n:
        result *= counter
        counter += 1
    return result

if __name__ == '__main__':
    sample_values = [0, 1, 5, 10]
    for val in sample_values:
        print(factorial(val))