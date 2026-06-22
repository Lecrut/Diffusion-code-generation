def calculate_power(base, exponent):
    result = base ** exponent
    return float(result)

if __name__ == '__main__':
    sample_base = 2.5
    sample_exponent = 3.0
    print(calculate_power(sample_base, sample_exponent))

    sample_base_neg = -2.0
    sample_exponent_int = 3
    print(calculate_power(sample_base_neg, sample_exponent_int))

    sample_base_frac = 4.0
    sample_exponent_frac = 0.5
    print(calculate_power(sample_base_frac, sample_exponent_frac))

    sample_base_zero = 0.0
    sample_exponent_pos = 5
    print(calculate_power(sample_base_zero, sample_exponent_pos))

    sample_base_one = 1.0
    sample_exponent_large = 100
    print(calculate_power(sample_base_one, sample_exponent_large))

    sample_base_small = 10.0
    sample_exponent_neg = -2
    print(calculate_power(sample_base_small, sample_exponent_neg))