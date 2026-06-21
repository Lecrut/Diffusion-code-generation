def get_first_element(lst):
    if not isinstance(lst, list):
        raise ValueError('Input must be a list')
    return lst[0] if lst else None

if __name__ == '__main__':
    SAMPLE_LIST = [1, 2, 3]
    EMPTY_LIST = []
    NON_LIST_INPUT = 'not a list'

    test_cases = [
        (SAMPLE_LIST, 'sample_list'),
        (EMPTY_LIST, 'empty_list'),
        (NON_LIST_INPUT, 'non_list_input')
    ]

    for value, name in test_cases:
        try:
            print(f"{name}: {get_first_element(value)}")
        except ValueError as e:
            print(f"{name}: {e}")