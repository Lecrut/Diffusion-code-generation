def calculate_power(base, exponent):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be an integer or float")
    if not isinstance(exponent, (int, float)):
        raise TypeError("Exponent must be an integer or float")
    return base ** exponent

if __name__ == '__main__':
    result = calculate_power(2, 10)
    print(result)