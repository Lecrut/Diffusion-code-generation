def secure_power(base, exponent):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number")
    if not isinstance(exponent, (int, float)):
        raise TypeError("Exponent must be a number")
    if base < 0 and not exponent.is_integer():
        raise ValueError("Negative base with non-integer exponent is not supported")
    if base < 0 and exponent < 0:
        raise ValueError("Negative base with negative exponent is not supported")
    
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    
    negative_exp = False
    if exponent < 0:
        negative_exp = True
        exponent = -exponent
    
    result = 1
    current_base = base
    exp = int(exponent)
    
    while exp > 0:
        if exp % 2 == 1:
            result *= current_base
        current_base *= current_base
        exp //= 2
    
    if negative_exp:
        return 1 / result
    return result

if __name__ == '__main__':
    print(secure_power(2, 10))
    print(secure_power(3, 3))
    print(secure_power(5, 0))
    print(secure_power(2, -3))
    print(secure_power(-2, 3))