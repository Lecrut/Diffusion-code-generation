def validate_exact_match(arg1, arg2):
    return arg1 == arg2
if __name__ == '__main__':
    sample_value1 = {'key': 'value'}
    sample_value2 = {'key': 'value'}
    sample_value3 = (1, 2, 3)
    sample_value4 = (1, 2, 4)
    result_dict = validate_exact_match(sample_value1, sample_value2)
    print(f'Result for dictionary comparison: {result_dict}')
    result_tuple = validate_exact_match(sample_value3, sample_value4)
    print(f'Result for tuple comparison: {result_tuple}')