def get_last_element(input_list):
    if not isinstance(input_list, list):
        raise TypeError('Input must be a list')
    if len(input_list) == 0:
        return None
    return input_list[-1]
if __name__ == '__main__':
    sample_data_1 = [1, 2, 3, 4, 5]
    sample_data_2 = []
    sample_data_3 = ['a', 'b', 'c']
    print(get_last_element(sample_data_1))
    print(get_last_element(sample_data_2))
    print(get_last_element(sample_data_3))