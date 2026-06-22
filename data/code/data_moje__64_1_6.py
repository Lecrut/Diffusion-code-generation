def calculate_power(base, exponent):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be an integer or float.")
    if not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer.")
    return base ** exponent

if __name__ == '__main__':
    sample_base = 2.5
    sample_exponent = 3
    result = calculate_power(sample_base, sample_exponent)
    print(result)