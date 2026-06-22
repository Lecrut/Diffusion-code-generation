def compare_two_simple_quantities_now_compare():
    sample_value_1 = 42
    sample_value_2 = 24
    if sample_value_1 > sample_value_2:
        return {'result': 'sample_value_1 is greater', 'values': [sample_value_1, sample_value_2]}
    elif sample_value_1 < sample_value_2:
        return {'result': 'sample_value_2 is greater', 'values': [sample_value_1, sample_value_2]}
    else:
        return {'result': 'both values are equal', 'values': [sample_value_1, sample_value_2]}

if __name__ == '__main__':
    result = compare_two_simple_quantities_now_compare()
    print(result)