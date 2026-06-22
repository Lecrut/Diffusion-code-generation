def get_first_element(lst):
    if not isinstance(lst, list):
        raise ValueError('Input must be a list')
    try:
        return lst[0]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_list = [1, 2, 3]
    empty_list = []
    non_list_input = 'not a list'
    
    test_cases = [
        (sample_list, 'sample_list'),
        (empty_list, 'empty_list'),
        (non_list_input, 'non_list_input')
    ]
    
    for value, name in test_cases:
        try:
            print(f"{name}: {get_first_element(value)}")
        except ValueError as e:
            print(f"{name}: {e}")