def filter_valid_entries(input_list):
    return [item for item in input_list if item is not None and item != '']

if __name__ == '__main__':
    sample_list = ['hello', '', None, 'world', None, '']
    filtered_list = filter_valid_entries(sample_list)
    print(filtered_list)