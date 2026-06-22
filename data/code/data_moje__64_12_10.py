def power(base, exponent):
    if exponent < 0:
        if base == 0:
            raise ZeroDivisionError("Cannot raise zero to a negative power")
        return 1.0 / power(base, -exponent)
    
    if exponent == 0:
        return 1.0
    
    if base == 0:
        return 0.0
    
    result = 1.0
    for _ in range(exponent):
        try:
            result = result * base
        except OverflowError:
            raise OverflowError("Result too large to represent as a float")
    
    return result

if __name__ == '__main__':
    print(power(2.0, 10))
    print(power(3.0, 3))
    print(power(5.0, 0))
    print(power(0.0, 5))