def power(base, exponent):
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise TypeError("Base and exponent must be numeric types")
    if isinstance(base, float) and base.is_integer():
        base = int(base)
    if isinstance(exponent, float) and exponent.is_integer():
        exponent = int(exponent)
    if isinstance(base, (int, float)) and base < 0 and isinstance(exponent, (int, float)) and exponent < 0:
        raise ValueError("Negative base with negative exponent is not supported")
    result = 1
    abs_exp = abs(exponent)
    if isinstance(abs_exp, float):
        result = base ** exponent
        return result
    current_base = base
    current_exp = abs_exp
    while current_exp > 0:
        if current_exp % 2 == 1:
            result *= current_base
        current_base *= current_base
        current_exp //= 2
    if exponent < 0:
        result = 1 / result
    return result

if __name__ == '__main__':
    print(power(2, 3))
    print(power(5, 0))
    print(power(2, -2))
    print(power(-3, 3))
    print(power(2.5, 3))
    try:
        power(-2, -3)
    except ValueError as e:
        print(e)
    try:
        power("2", 3)
    except TypeError as e:
        print(e)