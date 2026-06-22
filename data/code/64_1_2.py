def calculate_power(base, exponent):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be an integer or float")
    if not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer")
    return base ** exponent

if __name__ == '__main__':
    result1 = calculate_power(2, 3)
    print(result1)
    result2 = calculate_power(5.5, 2)
    print(result2)
    result3 = calculate_power(10, 0)
    print(result3)