def check_contradictory_combination(bool_list):
    n = len(bool_list)
    for i in range(n):
        for j in range(i + 1, n):
            if bool_list[i] and not bool_list[j]:
                return True
            if not bool_list[i] and bool_list[j]:
                return True
    return False
if __name__ == '__main__':
    test_cases = [
        ([True, True], False),
        ([False, False], False),
        ([True, False], True),
        ([True, True, True], False),
        ([False, False, False], False),
        ([True, False, True], True),
        ([True, True, False], True),
        ([False, True, True], True),
        ([True, True, True, True], False),
        ([False, False, False, False], False),
        ([True, False, False, True], True),
        ([True, True, False, False], True)
    ]
    for bool_list, expected in test_cases:
        result = check_contradictory_combination(bool_list)
        assert result == expected, f"Input: {bool_list}, Expected: {expected}, Got: {result}"
        print(f"Test passed for {bool_list}: Result {result}")