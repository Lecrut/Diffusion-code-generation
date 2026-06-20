def filter_valid_entries(input_list):
    filtered_list = [entry for entry in input_list if entry is not None and entry != '']
    return filtered_list

if __name__ == '__main__':
    sample_values = ['apple', '', None, 'banana', ' ', 'cherry']
    valid_entries = filter_valid_entries(sample_values)
    print(valid_entries)