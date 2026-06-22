def factorial(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == '__main__':
    sample_values = [0, 1, 5, 10]
    for value in sample_values:
        print(factorial(value))