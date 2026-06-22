import math

BASE_VALUE = 5.0
EXPONENT_VALUE = 2.0

def calculate_power(base, exponent):
    intermediate_base = float(base)
    intermediate_exponent = float(exponent)
    return math.pow(intermediate_base, intermediate_exponent)

if __name__ == '__main__':
    result = calculate_power(BASE_VALUE, EXPONENT_VALUE)
    print(result)