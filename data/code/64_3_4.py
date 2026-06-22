import math

def compute_power(base, exponent):
    return math.pow(base, exponent)

if __name__ == '__main__':
    base_value = 2.0
    exponent_value = 3.0
    result = compute_power(base_value, exponent_value)
    print(result)