def filter_valid_entries(input_list):
    return [entry for entry in input_list if entry is not None and entry != '']

if __name__ == '__main__':
    sample_values = ['apple', '', None, 'banana', ' ', 'cherry']
    valid_entries = filter_valid_entries(sample_values)
    print(valid_entries)