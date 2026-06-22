def calculate_power(base: float, exponent: int) -> float:
    if exponent == 0:
        return 1.0
    
    negative_exponent = exponent < 0
    exp = abs(exponent)
    
    result = 1.0
    current_product = base
    
    while exp > 0:
        if exp % 2 == 1:
            result *= current_product
        current_product *= current_product
        exp //= 2
    
    if negative_exponent:
        result = 1.0 / result
    
    return result

if __name__ == '__main__':
    print(calculate_power(2, 10))
    print(calculate_power(5, 0))
    print(calculate_power(2, -2))