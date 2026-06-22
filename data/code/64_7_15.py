import math

def calculate_power(base, exponent):
    if base == 0 and exponent <= 0:
        raise ZeroDivisionError("0 cannot be raised to a non-positive power")
    return float(base ** exponent)

if __name__ == '__main__':
    base_value = 2.0
    exponent_value = 0.5
    result = calculate_power(base_value, exponent_value)
    print(result)
    base_value = 10.0
    exponent_value = 2.5
    result = calculate_power(base_value, exponent_value)
    print(result)
    base_value = -8.0
    exponent_value = 1.0 / 3.0
    try:
        result = calculate_power(base_value, exponent_value)
        print(result)
    except ValueError:
        print("Error: Negative base with fractional exponent")