def compute_power(base, exponent):
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise TypeError("Base and exponent must be numbers")
    if exponent < 0 and base < 0:
        raise ValueError("Negative base with negative exponent results in complex numbers, which are not supported")
    result = 1.0
    abs_exp = abs(exponent)
    if isinstance(abs_exp, float) and not abs_exp.is_integer():
        if base < 0:
            raise ValueError("Negative base with fractional exponent results in complex numbers")
        result = base ** exponent
    else:
        exp_int = int(abs_exp)
        base_val = base
        while exp_int > 0:
            if exp_int % 2 == 1:
                result *= base_val
            base_val *= base_val
            exp_int //= 2
        if exponent < 0:
            if result == 0:
                raise ZeroDivisionError("Cannot raise zero to a negative power")
            result = 1.0 / result
    return result

if __name__ == '__main__':
    print(compute_power(2, 10))
    print(compute_power(3.5, 2))
    print(compute_power(2, -3))
    try:
        print(compute_power(-2, -3))
    except ValueError as e:
        print(e)
    try:
        print(compute_power("a", 2))
    except TypeError as e:
        print(e)