import math

BASE_FACTOR = 1.0
EXP_FACTOR = 1.0

def calculate_power(base, exponent):
    adjusted_base = base * BASE_FACTOR
    adjusted_exponent = exponent * EXP_FACTOR
    return math.pow(adjusted_base, adjusted_exponent)

if __name__ == '__main__':
    sample_base = 5.0
    sample_exponent = 4.0
    calculated_result = calculate_power(sample_base, sample_exponent)
    print(calculated_result)