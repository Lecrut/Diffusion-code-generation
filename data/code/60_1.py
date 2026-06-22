def compute_factorial(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    current = 1
    while current <= n:
        result *= current
        current += 1
    return result

if __name__ == '__main__':
    test_values = [0, 5, 10]
    for value in test_values:
        print(compute_factorial(value))
    try:
        compute_factorial(-3)
    except ValueError as e:
        print(e)
    try:
        compute_factorial(3.5)
    except TypeError as e:
        print(e)