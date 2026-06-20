def is_any_true(data, bool_list):
    return data or any(bool_list)

if __name__ == '__main__':
    test_cases = [
        (True, [False, False], True),
        (False, [True, False], True),
        (False, [False, True], True),
        (False, [False, False], False)
    ]
    
    for data, bool_list, expected in test_cases:
        result = is_any_true(data, bool_list)
        print(f"is_any_true({data}, {bool_list}) -> Expected: {expected}, Got: {result}")