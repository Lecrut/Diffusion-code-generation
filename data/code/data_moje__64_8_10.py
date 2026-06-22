def power(base, exponent):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be an integer or float.")
    if not isinstance(exponent, (int, float)):
        raise TypeError("Exponent must be an integer or float.")
    if exponent < 0 and base < 0:
        raise ValueError("Negative exponents are not allowed for negative bases.")
    if exponent < 0 and base == 0:
        raise ValueError("Exponent cannot be negative when base is zero.")
    if exponent == 0:
        return 1
    result = 1.0
    if exponent < 0:
        base = 1 / base
        exponent = -exponent
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent //= 2
    return result

if __name__ == '__main__':
    print(power(2, 10))
    print(power(5, -2))
    print(power(-3, 3))
    try:
        power(-2, -3)
    except ValueError as e:
        print(e)
    try:
        power("a", 2)
    except TypeError as e:
        print(e)