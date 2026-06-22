def compute_factorial(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    counter = 2
    while counter <= n:
        result *= counter
        counter += 1
    return result

if __name__ == '__main__':
    test_values = [0, 1, 5, 10, -1, 3.5, "string"]
    for value in test_values:
        try:
            result = compute_factorial(value)
            print(f"Factorial of {value} is {result}")
        except (TypeError, ValueError) as e:
            print(f"Error computing factorial of {value}: {e}")