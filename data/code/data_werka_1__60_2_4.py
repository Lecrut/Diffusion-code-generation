def get_last_item(data_list):
    if not data_list:
        raise IndexError("The list is empty")
    return data_list[-1]

if __name__ == '__main__':
    test_cases = {
        'case1': {'list': [1, 2, 3], 'expected': 3},
        'case2': {'list': ['a', 'b', 'c'], 'expected': 'c'},
        'case3': {'list': [], 'expected': None}
    }
    
    for case_name, test_case in test_cases.items():
        try:
            result = get_last_item(test_case['list'])
            print(f"Last item of {test_case['list']} (Case: {case_name}): {result}")
        except IndexError as e:
            if test_case['expected'] is None:
                print(f"Correctly caught error for empty list (Case: {case_name})")
            else:
                print(f"Error for case {case_name}: {e}")