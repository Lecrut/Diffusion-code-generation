import math

def compute_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    current_value = 1
    multiplier = 1
    while multiplier <= n:
        current_value *= multiplier
        multiplier += 1
    return current_value

if __name__ == '__main__':
    test_inputs = [3, 7, 12, 25]
    for val in test_inputs:
        print(compute_factorial(val))
    assert math.factorial(5) == compute_factorial(5)
    print(compute_factorial(5))