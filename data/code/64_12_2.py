def power(base, exponent):
    if not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer")
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number")

    result = 1.0
    negative_exp = exponent < 0
    exp = abs(exponent)

    for _ in range(exp):
        try:
            result *= base
            if abs(result) > 1e308:
                raise OverflowError("Result overflowed")
        except OverflowError:
            raise OverflowError("Result overflowed")

    if negative_exp:
        if result == 0:
            raise ZeroDivisionError("Cannot compute reciprocal of zero")
        result = 1.0 / result

    return result

if __name__ == '__main__':
    print(power(2.0, 10))
    print(power(3.5, 3))
    print(power(2.0, -3))
    print(power(0.5, 4))
    print(power(10.0, 0))