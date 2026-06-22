def calculate_power(base, exponent):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number")
    if not isinstance(exponent, (int, float)):
        raise TypeError("Exponent must be a number")
    if exponent < 0:
        if base == 0:
            raise ZeroDivisionError("Cannot raise zero to a negative power")
        return 1 / (base ** (-exponent))
    return base ** exponent

if __name__ == '__main__':
    print(calculate_power(2, 3))
    print(calculate_power(5, 0))
    print(calculate_power(2, -3))
    print(calculate_power(-2, 3))