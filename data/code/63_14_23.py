def get_first_element(lst):
    if not isinstance(lst, list):
        raise ValueError('Input must be a list')
    if len(lst) == 0:
        return None
    return lst[0]

if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3], 'sample_list'),
        ([], 'empty_list'),
        ('not a list', 'non_list_input')
    ]
    
    for value, name in test_cases:
        try:
            print(f"{name}: {get_first_element(value)}")
        except ValueError as e:
            print(f"{name}: {e}")