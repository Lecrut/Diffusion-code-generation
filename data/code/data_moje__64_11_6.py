def power_by_squaring(base, exponent):
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
    print(power_by_squaring(2, 10))
    print(power_by_squaring(3, 5))
    print(power_by_squaring(-2, 3))
    print(power_by_squaring(-3, 2))
    print(power_by_squaring(2, -2))
    print(power_by_squaring(-2, 4))