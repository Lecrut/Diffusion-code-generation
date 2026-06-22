def calculate_power(base: float, exponent: float) -> float:
    return base ** exponent

if __name__ == '__main__':
    result = calculate_power(2.0, 0.5)
    print(result)
    result2 = calculate_power(9.0, 0.5)
    print(result2)
    result3 = calculate_power(10.0, 3.0)
    print(result3)