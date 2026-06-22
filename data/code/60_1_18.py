def compute_factorial(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == '__main__':
    test_values = [0, 1, 5, 10, -1, 3.5]
    for value in test_values:
        try:
            print(f"Factorial of {value}: {compute_factorial(value)}")
        except Exception as e:
            print(f"Error calculating factorial of {value}: {e}")