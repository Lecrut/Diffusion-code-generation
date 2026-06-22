def compare_two_simple_quantities_now_compare():
    sample_value_1 = 42
    sample_value_2 = 24
    if sample_value_1 > sample_value_2:
        return "sample_value_1 is greater"
    elif sample_value_1 < sample_value_2:
        return "sample_value_2 is greater"
    else:
        return "both values are equal"

if __name__ == '__main__':
    result = compare_two_simple_quantities_now_compare()
    print(result)