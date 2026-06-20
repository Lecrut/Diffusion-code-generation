VALID_ENTRY = lambda x: x is not None and x != ''

def filter_valid_entries(input_list):
    return [entry for entry in input_list if VALID_ENTRY(entry)]

if __name__ == '__main__':
    sample_values = ['hello', '', None, 'world', ' ', 'test']
    print(filter_valid_entries(sample_values))