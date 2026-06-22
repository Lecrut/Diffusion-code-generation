def is_valid_list(input_value):
    return isinstance(input_value, list)

def get_first_element(lst):
    if not is_valid_list(lst):
        raise ValueError('Input must be a list')
    if len(lst) == 0:
        return None
    return lst[0]

if __name__ == '__main__':
    sample_values = {
        'valid_list': [4, 5, 6],
        'empty_list': [],
        'invalid_input': "not a list"
    }
    
    for key, value in sample_values.items():
        try:
            print(f"{key}: {get_first_element(value)}")
        except ValueError as e:
            print(f"{key}: {e}")