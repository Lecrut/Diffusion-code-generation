def calculate_power(base, exponent):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number")
    if not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer")
    return base ** exponent

if __name__ == '__main__':
    result1 = calculate_power(2, 10)
    result2 = calculate_power(3.5, 2)
    result3 = calculate_power(-2, 3)
    print(result1)
    print(result2)
    print(result3)