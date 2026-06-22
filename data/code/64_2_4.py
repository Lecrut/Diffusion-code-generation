def power(base, exponent):
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise TypeError("Base and exponent must be numeric types")
    if base == 0 and exponent < 0:
        raise ValueError("0 cannot be raised to a negative power")
    result = 1
    abs_exponent = abs(exponent)
    current_base = base
    remaining = abs_exponent
    while remaining > 0:
        if remaining % 2 == 1:
            result *= current_base
        current_base *= current_base
        remaining //= 2
    if exponent < 0:
        result = 1 / result
    return result

if __name__ == '__main__':
    print(power(2, 10))
    print(power(3, 0))
    print(power(2, -3))
    print(power(5.5, 2))
    print(power(-2, 3))