def calculate_power(base, exponent):
    if not isinstance(base, (int, float, complex)):
        raise TypeError("Base must be a number")
    if not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer")
    result = base ** exponent
    return result

if __name__ == '__main__':
    sample_base = 2
    sample_exponent = 10
    computed_value = calculate_power(sample_base, sample_exponent)
    print(computed_value)
    sample_base_float = 3.5
    sample_exponent_neg = -2
    computed_value_float = calculate_power(sample_base_float, sample_exponent_neg)
    print(computed_value_float)