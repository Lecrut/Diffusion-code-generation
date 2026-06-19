def access_elements():
    sample_tuple = (10, 20, 30, 40, 50)
    sample_dict = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
    last_element_tuple = sample_tuple[-1]
    values_list = next(iter(sample_dict.values()))
    if len(values_list) < 2:
        raise ValueError('Dictionary value list must contain at least two elements')
    second_to_last_value_dict = values_list[-2]
    return (last_element_tuple, second_to_last_value_dict)
if __name__ == '__main__':
    result = access_elements()
    print(result)