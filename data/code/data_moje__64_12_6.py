def power(base, exponent):
    if not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer")
    
    if exponent == 0:
        return 1
    
    is_negative_exponent = exponent < 0
    abs_exponent = abs(exponent)
    
    result = 1.0
    current_base = float(base)
    
    while abs_exponent > 0:
        if abs_exponent % 2 == 1:
            result *= current_base
            if not is_negative_exponent:
                try:
                    float.__mul__(result, 1)
                except OverflowError:
                    raise OverflowError("Result too large")
        
        abs_exponent //= 2
        current_base *= current_base
        if not is_negative_exponent:
            if current_base > float('inf') or (current_base != current_base and current_base == 0):
                if current_base == float('inf'):
                     raise OverflowError("Intermediate calculation overflowed")

    if is_negative_exponent:
        result = 1.0 / result
    
    return result

if __name__ == '__main__':
    base_val = 2.0
    exp_val = 10
    res = power(base_val, exp_val)
    print(res)