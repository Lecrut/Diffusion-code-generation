def calculate_power(base, n):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be an integer or float")
    if not isinstance(n, int):
        raise TypeError("Exponent must be an integer")
    return base ** n

if __name__ == '__main__':
    result = calculate_power(2, 10)
    print(result)