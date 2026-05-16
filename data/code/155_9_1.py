def sum_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
if __name__ == '__main__':
    test_case_1 = []
    expected_1 = 0
    result_1 = sum_list(test_case_1)
    assert result_1 == expected_1, f"Test Case 1 Failed: Expected {expected_1}, Got {result_1}"
    print(f"Test Case 1 Passed: Empty list. Result: {result_1}")
    test_case_2 = [1, 2, 3, 4, 5]
    expected_2 = 15
    result_2 = sum_list(test_case_2)
    assert result_2 == expected_2, f"Test Case 2 Failed: Expected {expected_2}, Got {result_2}"
    print(f"Test Case 2 Passed: Positive numbers. Result: {result_2}")
    test_case_3 = [-1, -2, -3]
    expected_3 = -6
    result_3 = sum_list(test_case_3)
    assert result_3 == expected_3, f"Test Case 3 Failed: Expected {expected_3}, Got {result_3}"
    print(f"Test Case 3 Passed: Negative numbers. Result: {result_3}")
    test_case_4 = [10, -5, 20, -1]
    expected_4 = 24
    result_4 = sum_list(test_case_4)
    assert result_4 == expected_4, f"Test Case 4 Failed: Expected {expected_4}, Got {result_4}"
    print(f"Test Case 4 Passed: Mixed numbers. Result: {result_4}")