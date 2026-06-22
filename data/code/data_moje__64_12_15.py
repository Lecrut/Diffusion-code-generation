def power(base, exponent):
    if not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer")
    
    if exponent == 0:
        return 1
    
    negative_exponent = exponent < 0
    abs_exponent = abs(exponent)
    
    result = 1.0
    current_base = float(base)
    
    while abs_exponent > 0:
        if abs_exponent & 1:
            result *= current_base
            if result == float('inf') or result == float('-inf'):
                raise OverflowError("Result overflowed")
        current_base *= current_base
        if current_base == float('inf') or current_base == float('-inf'):
            if abs_exponent > 1:
                raise OverflowError("Base overflowed during calculation")
        abs_exponent >>= 1
    
    if negative_exponent:
        if result == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = 1.0 / result
    
    return result

if __name__ == '__main__':
    base_val = 2.5
    exp_val = 3
    result = power(base_val, exp_val)
    print(result)