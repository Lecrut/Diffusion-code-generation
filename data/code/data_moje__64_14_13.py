import math

def calculate_power(base, exponent):
    if exponent == 0:
        return 1.0
    if exponent < 0:
        base = 1.0 / base
        exponent = -exponent
    result = 1.0
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent //= 2
    return result

if __name__ == '__main__':
    print(calculate_power(2, 10))
    print(calculate_power(5, 0))
    print(calculate_power(2, -2))