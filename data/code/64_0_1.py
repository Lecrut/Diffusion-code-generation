def binary_exponentiation(base, exponent):
    if exponent < 0:
        return 1 / binary_exponentiation(base, -exponent)
    
    result = 1
    current_base = base
    
    while exponent > 0:
        if exponent % 2 == 1:
            result *= current_base
        current_base *= current_base
        exponent //= 2
    
    return result

if __name__ == '__main__':
    print(binary_exponentiation(2, 10))
    print(binary_exponentiation(3, 5))
    print(binary_exponentiation(5, 0))
    print(binary_exponentiation(2, -3))