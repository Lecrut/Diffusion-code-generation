def power_with_overflow_check(base, exponent):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number")
    if not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer")

    if exponent == 0:
        return 1.0

    negative_exponent = False
    if exponent < 0:
        negative_exponent = True
        exponent = -exponent

    result = 1.0
    current_base = float(base)

    for _ in range(exponent):
        result *= current_base
        if result != result or abs(result) > 1e308:
            raise OverflowError("Computation resulted in overflow")

    if negative_exponent:
        if result == 0:
            raise ZeroDivisionError("Division by zero")
        result = 1.0 / result

    return result

if __name__ == '__main__':
    print(power_with_overflow_check(2.0, 10))
    print(power_with_overflow_check(3.0, -2))
    print(power_with_overflow_check(5.0, 0))
    print(power_with_overflow_check(-2.5, 3))
    try:
        power_with_overflow_check(10.0, 309)
    except OverflowError as e:
        print(str(e))