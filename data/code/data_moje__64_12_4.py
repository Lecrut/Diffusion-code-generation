def power(base, exponent):
    if not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer")
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number")
    
    if exponent == 0:
        return 1.0
    
    negative_exponent = False
    if exponent < 0:
        negative_exponent = True
        exponent = -exponent
    
    result = 1.0
    try:
        for _ in range(exponent):
            result *= base
            if abs(result) > 1.0e308:
                raise OverflowError("Result exceeds maximum float value")
    except OverflowError:
        raise
    
    if negative_exponent:
        if result == 0:
            raise ZeroDivisionError("Cannot raise zero to a negative power")
        result = 1.0 / result
    
    return result

if __name__ == '__main__':
    print(power(2.5, 3))
    print(power(10.0, -2))
    print(power(5.0, 0))