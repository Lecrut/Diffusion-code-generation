def integer_power(base, exponent):
    if exponent == 0:
        return 1
    negative_exponent = False
    if exponent < 0:
        negative_exponent = True
        exponent = -exponent
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent //= 2
    if negative_exponent:
        return 1 / result
    return result

if __name__ == '__main__':
    print(integer_power(2, 10))
    print(integer_power(-2, 10))
    print(integer_power(2, -10))
    print(integer_power(-2, 11))
    print(integer_power(0, 5))
    print(integer_power(5, 0))