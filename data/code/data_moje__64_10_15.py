def calculate_power(base, exponent):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number")
    if not isinstance(exponent, (int, float)):
        raise TypeError("Exponent must be a number")
    if base == 0 and exponent <= 0:
        raise ZeroDivisionError("Cannot raise zero to a negative or zero power")
    return base ** exponent

if __name__ == '__main__':
    print(calculate_power(2, 10))
    print(calculate_power(5, -2))
    print(calculate_power(3.5, 2))
    print(calculate_power(10, 0))
    print(calculate_power(0.5, 3))