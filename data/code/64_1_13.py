def power_with_check(base, exponent):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be an integer or float")
    if not isinstance(exponent, (int, float)):
        raise TypeError("Exponent must be an integer or float")
    return base ** exponent

if __name__ == '__main__':
    result1 = power_with_check(2, 10)
    result2 = power_with_check(3.5, 2)
    result3 = power_with_check(-2, 3)
    print(result1)
    print(result2)
    print(result3)