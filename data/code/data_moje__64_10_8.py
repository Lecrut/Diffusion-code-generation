def calculate_power(base, exponent):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number")
    if not isinstance(exponent, (int, float)):
        raise TypeError("Exponent must be a number")
    if isinstance(base, bool) or isinstance(exponent, bool):
        raise TypeError("Base and exponent must be numbers, not booleans")
    result = base ** exponent
    if result != result:
        raise ValueError("Result is not a number")
    return result

if __name__ == '__main__':
    print(calculate_power(2, 3))
    print(calculate_power(5, -2))
    print(calculate_power(0, 5))
    print(calculate_power(10, 0))
    print(calculate_power(-2, 3))
    print(calculate_power(2.5, 2))