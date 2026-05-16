def check_negativity(data: list[int]) -> list[bool]:
    return [x < 0 for x in data]
if __name__ == '__main__':
    test_list_1 = [1, -2, 3, -4, 5]
    expected_1 = [False, True, False, True, False]
    result_1 = check_negativity(test_list_1)
    assert result_1 == expected_1, f"Test 1 Failed: Expected {expected_1}, Got {result_1}"
    print("Test 1 Passed")
    test_list_2 = [10, 20, 30]
    expected_2 = [False, False, False]
    result_2 = check_negativity(test_list_2)
    assert result_2 == expected_2, f"Test 2 Failed: Expected {expected_2}, Got {result_2}"
    print("Test 2 Passed")
    test_list_3 = [-1, -5, 0, 100]
    expected_3 = [True, True, False, False]
    result_3 = check_negativity(test_list_3)
    assert result_3 == expected_3, f"Test 3 Failed: Expected {expected_3}, Got {result_3}"
    print("Test 3 Passed")
    test_list_4 = []
    expected_4 = []
    result_4 = check_negativity(test_list_4)
    assert result_4 == expected_4, f"Test 4 Failed: Expected {expected_4}, Got {result_4}"
    print("Test 4 Passed")