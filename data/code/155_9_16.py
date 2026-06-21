import numpy as np

def validate_input(numbers):
    if not isinstance(numbers, list) or not all(isinstance(x, int) for x in numbers):
        raise ValueError("Input must be a list of integers")

def sum_list(numbers):
    validate_input(numbers)
    return np.array(numbers).sum()

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