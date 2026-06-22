def get_first_element(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    return lst[0] if lst else None

if __name__ == '__main__':
    sample_data = {
        'list1': [1, 2, 3],
        'empty_list': [],
        'string_list': ['a', 'b', 'c'],
        'bool_list': [True, False],
        'none_list': [None]
    }
    for key, data in sample_data.items():
        print(f"{key}: {get_first_element(data)}")