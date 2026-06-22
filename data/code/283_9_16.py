def count_non_matching_elements(lst, data_type):
    return sum((1 for element in lst if not isinstance(element, data_type)))
if __name__ == '__main__':
    sample_list = [3.14, True, 2, 'hello', False]
    non_float_count = count_non_matching_elements(sample_list, float)
    print(non_float_count)