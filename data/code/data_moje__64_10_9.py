def calculate_power(base, exponent):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be an integer or float")
    if not isinstance(exponent, (int, float)):
        raise TypeError("Exponent must be an integer or float")
    
    if base == 0 and exponent < 0:
        raise ValueError("Cannot raise zero to a negative power")
    
    return base ** exponent

if __name__ == '__main__':
    print(calculate_power(2, 3))
    print(calculate_power(5, -2))
    print(calculate_power(10, 0))
    print(calculate_power(2.5, 2))
    try:
        print(calculate_power(0, -1))
    except ValueError as e:
        print(e)