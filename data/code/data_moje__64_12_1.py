def raise_to_exponent(base, exponent):
    if not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer")
    
    if exponent == 0:
        return 1
    
    negative_exponent = exponent < 0
    abs_exponent = abs(exponent)
    
    result = 1.0
    current_base = base
    
    while abs_exponent > 0:
        if abs_exponent % 2 == 1:
            result *= current_base
            if result == float('inf'):
                raise OverflowError("Result overflowed")
        current_base *= current_base
        if current_base == float('inf') and abs_exponent > 1:
            raise OverflowError("Base overflowed during calculation")
        abs_exponent //= 2
    
    if negative_exponent:
        result = 1.0 / result
        if result == float('inf'):
            raise OverflowError("Result overflowed during inversion")
            
    return result

if __name__ == '__main__':
    print(raise_to_exponent(2.0, 10))
    print(raise_to_exponent(5.0, 3))
    print(raise_to_exponent(2.0, -2))