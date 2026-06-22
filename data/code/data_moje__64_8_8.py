def power(base, exponent):
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise TypeError("Base and exponent must be numeric types")
    if isinstance(exponent, float) and not exponent.is_integer():
        raise ValueError("Exponent must be an integer")
    exponent = int(exponent)
    if base < 0 and exponent < 0:
        raise ValueError("Negative base with negative exponent is not supported")
    if exponent < 0:
        base = 1 / base
        exponent = -exponent
    result = 1
    current_base = base
    current_exp = exponent
    while current_exp > 0:
        if current_exp % 2 == 1:
            result *= current_base
        current_base *= current_base
        current_exp //= 2
    return result

if __name__ == '__main__':
    print(power(2, 10))
    print(power(3, 0))
    print(power(5, 3))
    try:
        power(-2, -3)
    except ValueError as e:
        print(str(e))
    try:
        power('2', 3)
    except TypeError as e:
        print(str(e))