def calculate_power(base: float, exponent: int) -> float:
    if exponent == 0:
        return 1
    
    negative_exponent = exponent < 0
    if negative_exponent:
        base = 1 / base
        exponent = -exponent
    
    result = 1
    current_product = base
    
    while exponent > 0:
        if exponent % 2 == 1:
            result *= current_product
        current_product *= current_product
        exponent //= 2
    
    return result

if __name__ == '__main__':
    test_cases = [
        (2, 10),
        (5, 0),
        (2, -2),
        (10, 3),
        (-2, 3)
    ]
    
    for base, exponent in test_cases:
        result = calculate_power(base, exponent)
        print(result)