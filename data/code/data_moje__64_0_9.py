def binary_exponentiation(base, exponent):
    if exponent < 0:
        base = 1 / base
        exponent = -exponent
    
    result = 1
    current_product = base
    
    while exponent > 0:
        if exponent % 2 == 1:
            result *= current_product
        exponent //= 2
        current_product *= current_product
    
    return result

if __name__ == '__main__':
    print(binary_exponentiation(2, 10))
    print(binary_exponentiation(5, 3))
    print(binary_exponentiation(2, -2))