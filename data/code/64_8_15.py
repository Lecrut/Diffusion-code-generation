def power(base, exponent):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number")
    if not isinstance(exponent, (int, float)):
        raise TypeError("Exponent must be a number")
    
    if base < 0 and exponent < 0:
        if exponent != int(exponent):
            raise ValueError("Negative base with non-integer negative exponent is not supported")
        if base == -1 and exponent % 2 != 0:
            raise ValueError("Result would be complex")
    
    if base < 0 and exponent > 0 and exponent != int(exponent):
        raise ValueError("Negative base with non-integer exponent is not supported")
        
    if base == 0 and exponent == 0:
        raise ValueError("0 raised to the power of 0 is undefined")
        
    if base == 0:
        if exponent > 0:
            return 0
        else:
            raise ZeroDivisionError("0 cannot be raised to a negative power")
            
    result = base ** exponent
    return result

if __name__ == '__main__':
    result = power(2, 3)
    print(result)
    
    result = power(-2, 3)
    print(result)
    
    result = power(2.5, 2)
    print(result)
    
    try:
        power(-2.5, 2)
    except ValueError as e:
        print(f"Error: {e}")
    
    try:
        power(0, 0)
    except ValueError as e:
        print(f"Error: {e}")
    
    try:
        power(2, "3")
    except TypeError as e:
        print(f"Error: {e}")