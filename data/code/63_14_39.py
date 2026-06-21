def get_first_element(lst):
    if not isinstance(lst, list):
        raise ValueError('Input must be a list')
    if not lst:
        return None
    return lst[0]

if __name__ == '__main__':
    sample_values = [
        ([1, 2, 3], 'sample_list'),
        ([], 'empty_list'),
        ('not a list', 'non_list_input')
    ]

    for value, name in sample_values:
        try:
            result = get_first_element(value)
            print(f"{name}: {result}")
        except ValueError as e:
            print(f"{name}: {e}")