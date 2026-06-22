def calculate_power(base, exponent):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a numeric type")
    if not isinstance(exponent, (int, float)):
        raise TypeError("Exponent must be a numeric type")
    return base ** exponent

if __name__ == '__main__':
    print(calculate_power(2, 10))
    print(calculate_power(9, -1))
    print(calculate_power(5, 0))