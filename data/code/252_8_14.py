def compare_two_simple_quantities_now_compare():
    sample_value_1 = 42
    sample_value_2 = 24

    if sample_value_1 > sample_value_2:
        return {'result': 'greater', 'value': sample_value_1}
    elif sample_value_1 < sample_value_2:
        return {'result': 'less', 'value': sample_value_2}
    else:
        return {'result': 'equal', 'value': sample_value_1}

if __name__ == '__main__':
    result = compare_two_simple_quantities_now_compare()
    print(result)