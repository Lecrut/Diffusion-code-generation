def power(base, exponent):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number")
    if not isinstance(exponent, (int, float)):
        raise TypeError("Exponent must be a number")
    return base ** exponent

if __name__ == '__main__':
    result = power(2, 10)
    print(result)