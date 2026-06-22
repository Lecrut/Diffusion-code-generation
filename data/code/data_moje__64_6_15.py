def power_bitwise(base, exponent):
    result = 1
    base = base % 1 if exponent == 0 else base
    if exponent < 0:
        base = 1 / base
        exponent = -exponent
    while exponent > 0:
        if exponent & 1:
            result *= base
        base *= base
        exponent >>= 1
    return result

if __name__ == '__main__':
    print(power_bitwise(2, 10))
    print(power_bitwise(3, 5))
    print(power_bitwise(5, 0))
    print(power_bitwise(2, -3))