def compute_factorial(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    current_value = 1
    multiplier = 1
    while multiplier <= n:
        current_value *= multiplier
        multiplier += 1
    return current_value

if __name__ == '__main__':
    sample_inputs = [0, 1, 6, 12, 15]
    for num in sample_inputs:
        print(compute_factorial(num))