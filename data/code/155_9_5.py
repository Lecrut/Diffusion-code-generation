def sum_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
if __name__ == '__main__':
    test_case_empty = []
    expected_empty = 0
    result_empty = sum_list(test_case_empty)
    assert result_empty == expected_empty, f"Empty list test failed: Expected {expected_empty}, Got {result_empty}"
    print(f"Test Case: Empty List")
    print(f"Input: {test_case_empty}")
    print(f"Result: {result_empty}")
    test_case_positive = [1, 2, 3, 4, 5]
    expected_positive = 15
    result_positive = sum_list(test_case_positive)
    assert result_positive == expected_positive, f"Positive numbers test failed: Expected {expected_positive}, Got {result_positive}"
    print(f"\nTest Case: Positive Numbers")
    print(f"Input: {test_case_positive}")
    print(f"Result: {result_positive}")
    test_case_negative = [-1, -5, 10]
    expected_negative = 4
    result_negative = sum_list(test_case_negative)
    assert result_negative == expected_negative, f"Negative numbers test failed: Expected {expected_negative}, Got {result_negative}"
    print(f"\nTest Case: Negative Numbers")
    print(f"Input: {test_case_negative}")
    print(f"Result: {result_negative}")
    test_case_mixed = [10, -5, 2, -8]
    expected_mixed = -1
    result_mixed = sum_list(test_case_mixed)
    assert result_mixed == expected_mixed, f"Mixed numbers test failed: Expected {expected_mixed}, Got {result_mixed}"
    print(f"\nTest Case: Mixed Numbers")
    print(f"Input: {test_case_mixed}")
    print(f"Result: {result_mixed}")