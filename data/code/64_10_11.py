def calculate_power(base, exponent):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number")
    if not isinstance(exponent, (int, float)):
        raise TypeError("Exponent must be a number")
    if exponent < 0:
        if base == 0:
            raise ZeroDivisionError("Cannot raise zero to a negative power")
    return base ** exponent

if __name__ == '__main__':
    result1 = calculate_power(2, 10)
    print(result1)
    result2 = calculate_power(5, -2)
    print(result2)
    result3 = calculate_power(10, 0)
    print(result3)