def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    acc = 1
    for current in range(1, n + 1):
        acc = acc * current
    return acc

if __name__ == '__main__':
    sample_values = [3, 7, 12]
    for val in sample_values:
        result = factorial(val)
        print(result)