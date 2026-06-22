def calculate_power(base, exponent):
    if exponent == 0:
        return 1
    if base == 0:
        return 0
    if exponent < 0:
        base = 1 / base
        exponent = -exponent
    result = 1
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
    print(calculate_power(3, 3))
    print(calculate_power(0, 5))
    print(calculate_power(10, 1))
    print(calculate_power(2.5, 3))