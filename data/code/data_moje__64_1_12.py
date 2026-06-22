def calculate_power(base: float, exponent: int) -> float:
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number.")
    if not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer.")
    return base ** exponent

if __name__ == '__main__':
    result = calculate_power(2, 10)
    print(result)