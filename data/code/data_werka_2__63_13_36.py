def get_first_element(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list")
    return lst[0] if lst else None

if __name__ == '__main__':
    sample_data = {
        'numbers': [1, 2, 3],
        'empty': [],
        'characters': ['a', 'b', 'c'],
        'booleans': [True, False],
        'single_none': [None]
    }
    for key, data in sample_data.items():
        print(f"{key}: {get_first_element(data)}")