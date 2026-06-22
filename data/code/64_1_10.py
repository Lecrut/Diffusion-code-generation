def calculate_power(base: complex, exponent: int) -> complex:
    if not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer")
    return base ** exponent

if __name__ == '__main__':
    result = calculate_power(2, 10)
    print(result)