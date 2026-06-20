def filter_valid_entries(input_list):
    return [item for item in input_list if item is not None and item != '']

if __name__ == '__main__':
    sample_data = ['hello', '', None, 'world', None, '']
    print(filter_valid_entries(sample_data))