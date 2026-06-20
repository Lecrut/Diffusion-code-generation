def is_any_true(input_bool, bool_list):
    return input_bool or any(bool_list)

if __name__ == '__main__':
    test_cases = [
        (True, [False, False]),
        (False, [False, False]),
        (False, [True, False]),
        (True, [True, True]),
        (False, [])
    ]
    
    for input_bool, bool_list in test_cases:
        result = is_any_true(input_bool, bool_list)
        print(f"Input: {input_bool}, {bool_list} -> Output: {result}")