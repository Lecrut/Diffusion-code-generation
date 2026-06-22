def calculate_power(base, exponent):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number")
    if not isinstance(exponent, (int, float)):
        raise TypeError("Exponent must be a number")
    if base == 0 and exponent < 0:
        raise ValueError("Cannot raise zero to a negative power")
    return base ** exponent

if __name__ == '__main__':
    result1 = calculate_power(2, 3)
    print(result1)

    result2 = calculate_power(5, -2)
    print(result2)

    result3 = calculate_power(10, 0)
    print(result3)

    result4 = calculate_power(2.5, 2)
    print(result4)

    result5 = calculate_power(-3, 3)
    print(result5)