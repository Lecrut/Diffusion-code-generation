def get_first_element(lst):
    if not isinstance(lst, list):
        raise TypeError('Input must be a list')
    return lst[0] if lst else None

if __name__ == '__main__':
    sample_data = {
        'list_with_numbers': [1, 2, 3],
        'empty_list': [],
        'list_with_strings': ['a', 'b', 'c'],
        'list_with_booleans': [True, False],
        'list_with_none': [None]
    }
    
    for key, value in sample_data.items():
        print(f"First element of {key}: {get_first_element(value)}")