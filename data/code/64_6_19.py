def power(base, exponent):
    if not isinstance(exponent, int) or exponent < 0:
        raise ValueError("Exponent must be a non-negative integer")
    if base == 0:
        return 0
    if exponent == 0:
        return 1
    
    result = 1
    current_base = base
    current_exponent = exponent
    
    while current_exponent > 0:
        if current_exponent & 1:
            result *= current_base
        current_base *= current_base
        current_exponent >>= 1
        
    return result

if __name__ == '__main__':
    base_val = 2
    exp_val = 10
    computed = power(base_val, exp_val)
    print(computed)