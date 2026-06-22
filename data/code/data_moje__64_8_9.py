def power(base, exponent):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number")
    if not isinstance(exponent, (int, float)):
        raise TypeError("Exponent must be a number")
    if base < 0 and not isinstance(exponent, int):
        raise ValueError("Negative base requires integer exponent for real results")
    if base < 0 and exponent % 2 != 0:
        raise ValueError("Negative base with non-integer exponent results in complex number")
    
    return base ** exponent

if __name__ == '__main__':
    result = power(2, 3)
    print(result)
    result2 = power(-2, 3)
    print(result2)
    result3 = power(0, 5)
    print(result3)