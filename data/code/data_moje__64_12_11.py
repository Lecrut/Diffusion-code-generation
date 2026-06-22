def power(base, exponent):
    if not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer")
    
    if exponent < 0:
        if base == 0:
            raise ValueError("Zero cannot be raised to a negative power")
        base = 1.0 / base
        exponent = -exponent
    
    result = 1.0
    current_base = base
    
    exp = exponent
    while exp > 0:
        if exp % 2 == 1:
            result *= current_base
        try:
            current_base *= current_base
        except OverflowError:
            raise OverflowError("Result overflowed during computation")
        exp //= 2
    
    if not result == result:
        raise OverflowError("Result is not a number due to overflow")
    if abs(result) > 1e308:
        raise OverflowError("Result overflowed")
    
    return result

if __name__ == '__main__':
    print(power(2.0, 10))
    print(power(3.0, 0))
    print(power(2.0, -3))
    print(power(0.5, 4))
    print(power(10.0, 3))