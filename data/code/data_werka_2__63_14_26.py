def get_first_element(lst):
    if not isinstance(lst, list):
        raise ValueError('Input must be a list')
    if len(lst) == 0:
        return None
    return lst[0]

if __name__ == '__main__':
    test_cases = {
        'sample_list': [1, 2, 3],
        'empty_list': [],
        'non_list_input': 'not a list'
    }
    
    for name, value in test_cases.items():
        try:
            result = get_first_element(value)
            print(f"{name}: {result}")
        except ValueError as e:
            print(f"{name}: Error - {e}")