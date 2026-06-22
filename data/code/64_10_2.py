def calculate_power(base, exponent):
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise TypeError("Base and exponent must be numeric types")
    if exponent == 0:
        return 1
    if base == 0:
        if exponent > 0:
            return 0
        else:
            raise ValueError("Cannot raise zero to a negative power")
    result = base ** exponent
    return result

if __name__ == '__main__':
    print(calculate_power(2, 3))
    print(calculate_power(5, 0))
    print(calculate_power(3, -2))
    print(calculate_power(-2, 4))
    print(calculate_power(10, 1))