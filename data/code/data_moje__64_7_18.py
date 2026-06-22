import math

def calculate_power(base, exponent):
    if base == 0 and exponent <= 0:
        raise ValueError("0 cannot be raised to a non-positive power")
    return math.pow(base, exponent)

if __name__ == '__main__':
    result = calculate_power(2.0, 0.5)
    print(result)