def calculate_power(base, exponent):
    if not isinstance(base, (int, float, complex)):
        raise TypeError("Base must be an integer, float, or complex number")
    if not isinstance(exponent, (int, float)):
        raise TypeError("Exponent must be an integer or float")
    result = base ** exponent
    return result

if __name__ == '__main__':
    base_value = 2.5
    exponent_value = 3
    computed_result = calculate_power(base_value, exponent_value)
    print(computed_result)
    another_base = 5
    another_exponent = 4
    another_result = calculate_power(another_base, another_exponent)
    print(another_result)
    negative_base = -3
    negative_exp = 2
    negative_result = calculate_power(negative_base, negative_exp)
    print(negative_result)
    zero_exp = 7
    zero_exp_result = calculate_power(zero_base := 10, zero_exp)
    print(zero_exp_result)