def filter_valid_entries(input_list):
    return [entry for entry in input_list if entry is not None and entry != '']

if __name__ == '__main__':
    sample_values = ['hello', '', None, 'world', None, '']
    filtered_values = filter_valid_entries(sample_values)
    print(filtered_values)