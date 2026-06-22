def calculate_power(base, exponent):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be an integer or float")
    if not isinstance(exponent, (int, float)):
        raise TypeError("Exponent must be an integer or float")
    
    if exponent < 0:
        if base == 0:
            raise ValueError("Cannot raise zero to a negative power")
        result = base ** exponent
        return result
    
    result = base ** exponent
    return result

if __name__ == '__main__':
    print(calculate_power(2, 3))
    print(calculate_power(5, -2))
    print(calculate_power(9, 0))