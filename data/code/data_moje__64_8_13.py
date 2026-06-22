def power(base, exponent):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number")
    if not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer")
    if exponent < 0 and base < 0:
        raise ValueError("Negative exponent with negative base is not allowed")
    if exponent < 0 and base == 0:
        raise ValueError("Zero raised to a negative power is undefined")
    
    result = 1
    abs_exponent = abs(exponent)
    current_base = base
    
    while abs_exponent > 0:
        if abs_exponent % 2 == 1:
            result *= current_base
        current_base *= current_base
        abs_exponent //= 2
    
    if exponent < 0:
        result = 1 / result
    
    return result

if __name__ == '__main__':
    print(power(2, 10))
    print(power(5, 0))
    print(power(2, -3))
    print(power(3.5, 2))
    print(power(-2, 3))