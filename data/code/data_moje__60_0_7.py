def _validate_non_negative_integer(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")

def factorial(n):
    _validate_non_negative_integer(n)
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    test_values = [0, 1, 5, 20, 50]
    for value in test_values:
        print(factorial(value))