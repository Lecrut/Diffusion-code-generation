def power(base, exponent):
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise TypeError("Base and exponent must be int or float")
    if exponent == 0:
        return 1
    if isinstance(exponent, int) and exponent < 0:
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
    print(power(2, 10))
    print(power(3.5, 4))
    print(power(5, -2))
    print(power(7, 0))
    print(power(2.0, 3))