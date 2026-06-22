def calculate_factorial(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    test_values = [5, 0, 1, 10]
    for val in test_values:
        print(calculate_factorial(val))
    try:
        calculate_factorial(-3)
    except ValueError as e:
        print(e)
    try:
        calculate_factorial(3.5)
    except TypeError as e:
        print(e)