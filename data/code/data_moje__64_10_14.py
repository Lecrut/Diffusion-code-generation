def calculate_power(base, exponent):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be an int or float")
    if not isinstance(exponent, (int, float)):
        raise TypeError("Exponent must be an int or float")
    result = base ** exponent
    return result

if __name__ == '__main__':
    print(calculate_power(2, 3))
    print(calculate_power(5, -2))
    print(calculate_power(-3, 2))
    print(calculate_power(10, 0))
    print(calculate_power(2.5, 3))