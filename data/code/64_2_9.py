def optimized_power(base, exponent):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be an integer or float")
    if not isinstance(exponent, (int, float)):
        raise TypeError("Exponent must be an integer or float")
    if exponent == 0:
        return 1.0 if isinstance(base, float) else 1
    if base == 0:
        return 0.0 if isinstance(base, float) else 0
    if isinstance(exponent, int) and exponent > 0:
        result = 1
        b = base
        e = exponent
        while e > 0:
            if e % 2 == 1:
                result *= b
            b *= b
            e //= 2
        return result
    try:
        result = base ** exponent
        return result
    except OverflowError:
        raise OverflowError("Result too large to compute")

if __name__ == '__main__':
    print(optimized_power(2, 10))
    print(optimized_power(2.5, 3))
    print(optimized_power(5, -2))
    print(optimized_power(3.14, 2))
    print(optimized_power(0, 5))
    print(optimized_power(7, 0))