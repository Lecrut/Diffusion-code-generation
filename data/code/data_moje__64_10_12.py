def calculate_power(base, exponent):
    return base ** exponent

if __name__ == '__main__':
    sample_base_1 = 2
    sample_exponent_1 = 3
    result_1 = calculate_power(sample_base_1, sample_exponent_1)
    print(result_1)

    sample_base_2 = 5
    sample_exponent_2 = -2
    result_2 = calculate_power(sample_base_2, sample_exponent_2)
    print(result_2)

    sample_base_3 = 10
    sample_exponent_3 = 0
    result_3 = calculate_power(sample_base_3, sample_exponent_3)
    print(result_3)