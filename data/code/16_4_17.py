def check_all_positive(numbers):
    """
    Checks if all numbers in the list are positive (greater than 0).
    
    Optimization: Returns immediately upon finding a non-positive number,
    avoiding unnecessary iterations through the rest of the list.
    
    Args:
        numbers (list[float]): A list of numeric values to check.
        
    Returns:
        bool: True if all elements are positive, False otherwise.
    """
    for num in numbers:
        if num <= 0:
            return False
    return True

if __name__ == '__main__':
    # Sample test cases with no user input or external dependencies
    sample_cases = [
        ([1, 2, 3], True),
        ([-1, 2, 3], False),
        ([0.5, -0.1, 4], False),
        ([], True),  # Empty list is considered to have all elements positive by convention here
    ]

    for i, test_input in enumerate(sample_cases):
        result = check_all_positive(test_input[0])
        expected = test_input[1]
        
        if result == expected:
            print(f"Test case {i + 1}: PASSED")
        else:
            print(f"Test case {i + 1}: FAILED (Expected {expected}, got {result})")

    # Additional manual verification example
    test_list = [3, -5, 7]
    status = check_all_positive(test_list)
    if not isinstance(status, bool):
        raise TypeError("Function must return a boolean.")