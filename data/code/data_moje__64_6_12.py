def power_bitwise(base, exponent):
    if exponent < 0:
        base = 1 / base
        exponent = -exponent
    result = 1
    current_base = base
    while exponent > 0:
        if exponent & 1:
            result *= current_base
        current_base *= current_base
        exponent >>= 1
    return result

if __name__ == '__main__':
    print(power_bitwise(2, 10))
    print(power_bitwise(3, 0))
    print(power_bitwise(5, 3))
    print(power_bitwise(2, -3))
    print(power_bitwise(0, 5))
    print(power_bitwise(1, 100))