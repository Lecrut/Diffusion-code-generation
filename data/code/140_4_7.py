def is_valid_entry(entry):
    return entry is not None and entry != ''

def filter_valid_entries(input_list):
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list")
    
    return [entry for entry in input_list if is_valid_entry(entry)]

if __name__ == '__main__':
    sample_values = ['hello', '', None, 'world', ' ', 'test']
    print(filter_valid_entries(sample_values))