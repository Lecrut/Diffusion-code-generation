def compute_factorial(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative")
    if n == 0:
        return 1
    result = 1
    current = 1
    while current <= n:
        result *= current
        current += 1
    return result

if __name__ == '__main__':
    test_values = [0, 1, 5, 10, -1, 3.14, "string"]
    for val in test_values:
        try:
            output = compute_factorial(val)
            print(f"Factorial of {val} is {output}")
        except (TypeError, ValueError) as e:
            print(f"Error for {val}: {e}")