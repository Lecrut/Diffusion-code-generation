def get_first_element(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    return lst[0] if lst else None

if __name__ == '__main__':
    sample_data = {
        'list_with_numbers': [10, 20, 30],
        'empty_list': [],
        'list_with_strings': ['apple', 'banana', 'cherry'],
        'list_with_booleans': [True, False, True],
        'list_with_none': [None]
    }
    
    for key, data in sample_data.items():
        print(f"First element of {key}: {get_first_element(data)}")