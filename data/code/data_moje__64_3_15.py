import math

def calculate_exponent(base, exp):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number")
    if not isinstance(exp, (int, float)):
        raise TypeError("Exponent must be a number")
    return math.pow(base, exp)

if __name__ == '__main__':
    base_val = 5.0
    power_val = 2.0
    output = calculate_exponent(base_val, power_val)
    print(output)