def power(base, exponent):
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise TypeError("Base and exponent must be numeric types")
    if isinstance(base, bool) or isinstance(exponent, bool):
        raise TypeError("Base and exponent must be numeric types")
    if base < 0 and not exponent.is_integer():
        raise ValueError("Negative base with non-integer exponent is not supported")
    if base < 0 and exponent < 0:
        raise ValueError("Negative base with negative exponent is not supported")
    if exponent < 0:
        raise ValueError("Exponent must be non-negative")
    result = 1
    for _ in range(int(exponent)):
        result *= base
    return result

if __name__ == '__main__':
    print(power(2, 10))
    print(power(3, 3))
    print(power(5, 0))
    try:
        power(-2, -3)
    except ValueError as e:
        print(e)
    try:
        power("2", 3)
    except TypeError as e:
        print(e)