import sys

def power_float_int(base, exponent):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number")
    if not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer")

    if exponent < 0:
        if base == 0:
            raise ZeroDivisionError("0 cannot be raised to a negative power")
        base = 1.0 / base
        exponent = -exponent

    result = 1.0
    current_base = base

    while exponent > 0:
        if exponent % 2 == 1:
            result *= current_base
            if abs(result) > sys.float_info.max:
                raise OverflowError("Result overflowed")
        current_base *= current_base
        if exponent > 1 and abs(current_base) > sys.float_info.max:
            if exponent > 1:
                raise OverflowError("Intermediate value overflowed")
        exponent //= 2

    if abs(result) > sys.float_info.max:
        raise OverflowError("Result overflowed")

    return result

if __name__ == '__main__':
    test_cases = [
        (2.0, 10),
        (3.5, -2),
        (10.0, 0),
        (-2.0, 3),
        (0.5, 4),
        (1.5, 100),
    ]

    for base, exp in test_cases:
        try:
            res = power_float_int(base, exp)
            print(f"{base}^{exp} = {res}")
        except Exception as e:
            print(f"{base}^{exp} raised {type(e).__name__}: {e}")