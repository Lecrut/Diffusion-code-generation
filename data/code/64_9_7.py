def calculate_power(base: float, exponent: float) -> float:
    return base ** exponent

if __name__ == '__main__':
    base_value = 2.0
    exponent_value = 3.0
    result = calculate_power(base_value, exponent_value)
    print(result)