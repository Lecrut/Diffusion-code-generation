def power(base, exponent):
    if isinstance(exponent, int) and exponent >= 0:
        result = 1
        current_base = base
        exp = exponent
        while exp > 0:
            if exp % 2 == 1:
                result *= current_base
            current_base *= current_base
            exp //= 2
        return result
    else:
        if base < 0 and isinstance(exponent, float) and exponent != int(exponent):
            raise ValueError("Cannot raise negative base to non-integer exponent")
        if base == 0 and exponent <= 0:
            raise ZeroDivisionError("0 raised to a non-positive power is undefined")
        return pow(base, exponent)

if __name__ == '__main__':
    print(power(2, 10))
    print(power(3, 0))
    print(power(5, -2))
    print(power(2.5, 3))
    print(power(4, 0.5))
    print(power(-2, 3))
    print(power(10, 2.3))