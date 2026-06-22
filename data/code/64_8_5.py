def power(base, exponent):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number")
    if not isinstance(exponent, (int, float)):
        raise TypeError("Exponent must be a number")
    
    if base < 0 and isinstance(exponent, float) and exponent != int(exponent):
        raise ValueError("Negative base with non-integer exponent results in complex number")
    
    if base < 0 and exponent < 0:
        if isinstance(exponent, float) and exponent == int(exponent):
            raise ValueError("Negative base with negative integer exponent results in complex number")
        elif not isinstance(exponent, (int, float)):
            raise TypeError("Exponent must be a number")
        else:
            raise ValueError("Negative base with negative exponent is not allowed in real numbers")
            
    return base ** exponent

if __name__ == '__main__':
    print(power(2, 10))
    print(power(9, 0.5))
    print(power(-2, 3))
    print(power(5, -2))