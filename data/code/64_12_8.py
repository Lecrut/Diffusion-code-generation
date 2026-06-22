def power(base, exponent):
    if not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer")
    if base == 0 and exponent < 0:
        raise ValueError("Cannot raise zero to a negative exponent")
    if exponent < 0:
        base = 1.0 / base
        exponent = -exponent
    result = 1.0
    for _ in range(exponent):
        result *= base
        if abs(result) > 1.8e308:
            raise OverflowError("Result exceeds maximum float value")
    return result

if __name__ == '__main__':
    print(power(2.0, 10))
    print(power(3.0, -2))
    print(power(5.0, 0))
    print(power(-2.0, 3))