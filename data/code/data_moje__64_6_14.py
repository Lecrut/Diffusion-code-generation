def power(base, exponent):
    if exponent < 0:
        base = 1 / base
        exponent = -exponent
    
    result = 1
    current_base = base
    
    while exponent > 0:
        if exponent & 1:
            result *= current_base
        current_base *= current_base
        exponent >>= 1
        
    return result

if __name__ == '__main__':
    result = power(2, 10)
    print(result)