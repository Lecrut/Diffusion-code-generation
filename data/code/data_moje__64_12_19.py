def power(base, exponent):
    if not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer")
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number")
    
    result = 1.0
    n = exponent
    if n < 0:
        if base == 0:
            raise ZeroDivisionError("Cannot raise zero to a negative power")
        n = -n
    
    for _ in range(n):
        result *= base
        if abs(result) > 1e308:
            raise OverflowError("Result exceeds floating point range")
    
    if exponent < 0:
        result = 1.0 / result
    
    return result

if __name__ == '__main__':
    print(power(2.5, 3))
    print(power(5.0, -2))
    print(power(-3.0, 4))