def calculate_power(base, exponent):
    if base == 0 and exponent <= 0:
        return 0.0
    return float(base ** exponent)

if __name__ == '__main__':
    result = calculate_power(2.0, 3.0)
    print(result)
    result = calculate_power(9.0, 0.5)
    print(result)
    result = calculate_power(10.0, -2.0)
    print(result)