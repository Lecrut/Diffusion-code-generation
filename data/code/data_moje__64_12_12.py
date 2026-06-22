def safe_power(base, exponent):
    if exponent < 0:
        if base == 0:
            raise ZeroDivisionError("0 cannot be raised to a negative power")
        try:
            result = safe_power(base, -exponent)
            return 1.0 / result
        except OverflowError:
            raise OverflowError("Result is too large for standard float representation")
    result = 1.0
    for _ in range(exponent):
        result *= base
        if result != result:
            raise OverflowError("Result is not a valid number")
        if (base != 0 and result > 1.7976931348623157e+308) or (base != 0 and result < -1.7976931348623157e+308):
            raise OverflowError("Result is too large for standard float representation")
    return result

if __name__ == '__main__':
    print(safe_power(2.0, 10))
    print(safe_power(2.0, -5))
    print(safe_power(5.0, 3))
    print(safe_power(0.5, 3))
    try:
        print(safe_power(10.0, 500))
    except OverflowError as e:
        print(e)