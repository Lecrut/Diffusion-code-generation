def calculate_power(base, exponent):
    if base == 0:
        if exponent > 0:
            return 0.0
        elif exponent < 0:
            return float('inf')
        else:
            return 1.0
    result = abs(base) ** abs(exponent)
    if base < 0 and exponent != int(exponent):
        return float('nan')
    if base < 0 and int(exponent) % 2 == 1:
        result = -result
    return float(result)

if __name__ == '__main__':
    print(calculate_power(2, 3))
    print(calculate_power(2, -3))
    print(calculate_power(4, 0.5))
    print(calculate_power(-2, 3))
    print(calculate_power(-2, 0.5))
    print(calculate_power(0, 5))
    print(calculate_power(0, -1))
    print(calculate_power(0, 0))
    print(calculate_power(9, 2.5))
    print(calculate_power(-3, 2))