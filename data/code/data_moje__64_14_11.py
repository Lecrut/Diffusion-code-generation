def calculate_power(base, exponent):
    if exponent == 0:
        return 1
    
    is_negative_exponent = exponent < 0
    exp = abs(exponent)
    
    result = 1
    current_base = base
    
    while exp > 0:
        if exp % 2 == 1:
            result *= current_base
        current_base *= current_base
        exp //= 2
    
    if is_negative_exponent:
        return 1 / result
    
    return result

if __name__ == '__main__':
    print(calculate_power(2, 10))
    print(calculate_power(5, 0))
    print(calculate_power(2, -2))
    print(calculate_power(10.5, 2))
    print(calculate_power(-3, 3))