def _calculate_non_negative_power(base, exp):
    result = 1
    current_base = base
    while exp > 0:
        if exp & 1:
            result *= current_base
        current_base *= current_base
        exp >>= 1
    return result

def calculate_integer_power(base, exp):
    if not isinstance(base, int) or not isinstance(exp, int):
        raise TypeError("Both base and exponent must be integers")
    
    if exp == 0:
        return 1
    
    if exp < 0:
        if base == 0:
            raise ZeroDivisionError("0 cannot be raised to a negative power")
        positive_result = _calculate_non_negative_power(base, -exp)
        return 1 // positive_result
    
    return _calculate_non_negative_power(base, exp)

if __name__ == '__main__':
    print(calculate_integer_power(2, 10))
    print(calculate_integer_power(-5, 3))
    print(calculate_integer_power(7, -1))
    print(calculate_integer_power(-2, 8))
    print(calculate_integer_power(0, 5))