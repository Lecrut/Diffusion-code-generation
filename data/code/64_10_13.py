def calculate_power(base, exponent):
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise TypeError("Base and exponent must be numbers")
    if isinstance(base, bool) or isinstance(exponent, bool):
        raise TypeError("Base and exponent must be numbers, not booleans")
    result = base ** exponent
    return result

if __name__ == '__main__':
    sample_base_1 = 2
    sample_exponent_1 = 3
    result_1 = calculate_power(sample_base_1, sample_exponent_1)
    print(result_1)

    sample_base_2 = 5
    sample_exponent_2 = -2
    result_2 = calculate_power(sample_base_2, sample_exponent_2)
    print(result_2)

    sample_base_3 = -3
    sample_exponent_3 = 3
    result_3 = calculate_power(sample_base_3, sample_exponent_3)
    print(result_3)

    sample_base_4 = 10
    sample_exponent_4 = 0
    result_4 = calculate_power(sample_base_4, sample_exponent_4)
    print(result_4)

    sample_base_5 = 2.5
    sample_exponent_5 = 2.0
    result_5 = calculate_power(sample_base_5, sample_exponent_5)
    print(result_5)