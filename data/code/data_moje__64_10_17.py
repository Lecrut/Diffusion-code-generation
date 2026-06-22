def calculate_power(base, exponent):
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise TypeError("Base and exponent must be numeric types.")
    if base == 0 and exponent < 0:
        raise ValueError("Cannot raise zero to a negative power.")
    return base ** exponent

if __name__ == '__main__':
    print(calculate_power(2, 3))
    print(calculate_power(5, -1))
    print(calculate_power(2.5, 2))
    print(calculate_power(10, 0))
    print(calculate_power(-3, 3))
    print(calculate_power(0, 5))