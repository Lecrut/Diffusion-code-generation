def check_all_positive(numbers):
    """
    Checks if all numbers in the list are positive.
    
    Args:
        numbers (list): A list of numerical values.
        
    Returns:
        bool: True if all numbers are greater than zero, False otherwise.
             An empty list is considered to have all elements satisfy the condition (True).
    """
    # Optimization: Early exit as soon as a non-positive number is found.
    for num in numbers:
        if num <= 0:
            return False
    
    return True

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_cases = [
        ([1, 2, 3], True),
        ([-1, 2, 3], False),
        ([0, -5, 4], False),
        ([], True),          # Edge case: empty list should return True based on universal quantification logic
        ([0.5, 1.7, 2.9], True),
    ]

    for test_input, expected_result in sample_cases:
        result = check_all_positive(test_input)
        status = "PASS" if result == expected_result else "FAIL"
        print(f"{status} | Input: {test_input} | Expected: {expected_result} | Got: {result}")