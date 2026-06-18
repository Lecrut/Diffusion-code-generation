def check_all_positive(numbers):
    """
    Returns True if all numbers in the list are positive, False otherwise.
    Optimized to stop at the first non-positive number found.
    
    Args:
        numbers (list): A list of numeric values.
        
    Returns:
        bool: True if all elements > 0, else False.
    """
    for num in numbers:
        if num <= 0:
            return False
    return True

if __name__ == '__main__':
    # Sample test cases with hard-coded values (no external input or files)
    sample_cases = [
        ([1, 2, 3], True),
        ([5, -1, 7], False),
        ([0.5, 1.2], True),
        ([-3, -4, -5], False),
        ([-1], False),
        ([], True)  # Empty list considered as all positive vacuously true per logic flow below
    ]

    for i, (test_list, expected_result) in enumerate(sample_cases):
        result = check_all_positive(test_list)
        status = "PASS" if result == expected_result else "FAIL"
        print(f"Test {i + 1}: Input={test_list}, Expected={expected_result}, Got={result} -> [{status}]")