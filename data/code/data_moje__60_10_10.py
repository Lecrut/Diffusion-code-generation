def calculate_factorial(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result

if __name__ == '__main__':
    sample_values = [0, 1, 5, 10]
    for val in sample_values:
        print(f"Factorial of {val}: {calculate_factorial(val)}")