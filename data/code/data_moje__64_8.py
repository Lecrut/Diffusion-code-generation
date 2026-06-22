def power(base, exponent):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be an integer or float.")
    if not isinstance(exponent, (int, float)):
        raise TypeError("Exponent must be an integer or float.")
    
    if exponent < 0:
        if base < 0:
            raise ValueError("Negative base with negative exponent is not allowed.")
        if base == 0:
            raise ZeroDivisionError("Cannot raise zero to a negative power.")
    
    return base ** exponent

if __name__ == '__main__':
    result = power(2, 3)
    print(result)
    result2 = power(-2, 4)
    print(result2)
    result3 = power(5, -1)
    print(result3)