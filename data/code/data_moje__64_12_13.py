def power(base, exponent):
    if exponent < 0:
        base = 1 / base
        exponent = -exponent
    
    if exponent == 0:
        return 1
    
    result = 1
    current_base = base
    
    while exponent > 0:
        if exponent % 2 == 1:
            try:
                result = result * current_base
            except OverflowError:
                raise OverflowError("Result exceeds float capacity")
        
        try:
            current_base = current_base * current_base
        except OverflowError:
            if exponent == 1:
                raise OverflowError("Base squared exceeds float capacity")
            break
        
        exponent = exponent // 2
    
    return result

if __name__ == '__main__':
    result = power(2.0, 10)
    print(result)