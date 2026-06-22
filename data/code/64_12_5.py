def power(base, exp):
    if not isinstance(exp, int):
        raise TypeError("Exponent must be an integer")
    if base == 0 and exp < 0:
        raise ZeroDivisionError("Zero cannot be raised to a negative exponent")
    if exp < 0:
        base = 1.0 / base
        exp = -exp
    result = 1.0
    try:
        for _ in range(exp):
            result *= base
            if abs(result) > 1.8e308:
                raise OverflowError("Result too large")
    except OverflowError:
        raise
    return result

if __name__ == '__main__':
    print(power(2.0, 10))
    print(power(3.0, 3))
    print(power(2.5, 0))
    print(power(1.5, -2))
    try:
        power(2.0, 1000)
    except OverflowError as e:
        print(str(e))