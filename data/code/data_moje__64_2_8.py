def power(base, exponent):
    if isinstance(exponent, int) and exponent >= 0:
        result = 1
        b = base
        exp = exponent
        while exp > 0:
            if exp % 2 == 1:
                result *= b
            b *= b
            exp //= 2
        return result
    if isinstance(exponent, int) and exponent < 0:
        if base == 0:
            raise ZeroDivisionError("0 cannot be raised to a negative power")
        result = 1
        b = base
        exp = -exponent
        while exp > 0:
            if exp % 2 == 1:
                result *= b
            b *= b
            exp //= 2
        return 1 / result
    return base ** exponent

if __name__ == '__main__':
    print(power(2, 10))
    print(power(2, -2))
    print(power(2.5, 3))
    print(power(0, 0))
    print(power(5, 0))