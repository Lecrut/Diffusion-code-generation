def integer_power(base, exponent):
    if exponent == 0:
        return 1
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
    print(integer_power(2, 10))
    print(integer_power(-3, 3))
    print(integer_power(5, -2))
    print(integer_power(-2, -3))
    print(integer_power(0, 5))
    print(integer_power(7, 0))