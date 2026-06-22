def calculate_nth_power(base, exponent):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be an integer or float")
    if not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer")
    return base ** exponent

if __name__ == '__main__':
    print(calculate_nth_power(2, 3))
    print(calculate_nth_power(5, 0))
    print(calculate_nth_power(3, 4))