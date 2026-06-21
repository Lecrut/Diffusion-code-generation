def get_first_element(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    return lst[0] if lst else None

if __name__ == '__main__':
    sample_data = {
        'numbers': [1, 2, 3],
        'empty': [],
        'characters': ['a', 'b', 'c'],
        'booleans': [True, False],
        'none_value': [None]
    }
    for description, data in sample_data.items():
        print(f"{description}: {get_first_element(data)}")