def check_contradictory_combination(bool_list):
    n = len(bool_list)
    for i in range(n):
        for j in range(i + 1, n):
            if bool_list[i] != bool_list[j]:
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
        ([False, True, False], True),
        ([], False),
        ([True], False),
        ([False], False)
    ]
    for bool_list, expected in test_cases:
        result = check_contradictory_combination(bool_list)
        assert result == expected, f"Input: {bool_list}, Expected: {expected}, Got: {result}"
        print(f"Input: {bool_list}, Result: {result}, Expected: {expected} - Passed")
    print("All test cases passed.")