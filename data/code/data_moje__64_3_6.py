import math

def _validate_exponent(exponent):
    if math.isinf(exponent):
        raise OverflowError("Exponent is infinite")
    if math.isnan(exponent):
        raise ValueError("Exponent is NaN")

def calculate_power(base, exponent):
    _validate_exponent(exponent)
    return math.pow(base, exponent)

if __name__ == '__main__':
    base_val = 3.14
    exponent_val = 2
    calculated_value = calculate_power(base_val, exponent_val)
    print(calculated_value)