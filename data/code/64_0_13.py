def power(base: int, exponent: int) -> int:
    if exponent == 0:
        return 1
    if base == 0:
        return 0
    if base == 1:
        return 1
    if base == -1:
        return 1 if exponent % 2 == 0 else -1
    
    is_negative_exponent = exponent < 0
    abs_exponent = abs(exponent)
    
    result = 1
    current_base = base
    
    while abs_exponent > 0:
        if abs_exponent % 2 == 1:
            result *= current_base
        current_base *= current_base
        abs_exponent //= 2
        
    if is_negative_exponent:
        return 1 / result
    
    return result

if __name__ == '__main__':
    print(power(2, 10))
    print(power(3, 0))
    print(power(5, 3))
    print(power(-2, 4))
    print(power(2, -2))