def power_with_type_check(base: int, exponent: int) -> int:
    if not isinstance(base, int):
        raise TypeError("Base must be an integer")
    if not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer")
    return base ** exponent

if __name__ == '__main__':
    sample_base = 5
    sample_exponent = 3
    result = power_with_type_check(sample_base, sample_exponent)
    print(result)
    sample_base_negative = -2
    sample_exponent_negative = 4
    result_negative = power_with_type_check(sample_base_negative, sample_exponent_negative)
    print(result_negative)