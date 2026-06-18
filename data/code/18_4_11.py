def is_max_greater_than_second_to_last(numbers):
    """
    Returns True if the maximum value in the list is greater than 
    the second-to-last element, otherwise False.

    Args:
        numbers (list of int or float): List of numerical values.

    Returns:
        bool: Boolean indicating whether max > second_to_last.
    
    Note: If the list has fewer than 2 elements, this will return 
    True if there is a single element (max equals itself) and no second-to-last,
    or False otherwise based on logical interpretation of 'greater than'.
    """
    if len(numbers) == 0:
        # Edge case: empty list has no max or second to last. Conventionally treat as False for safety.
        return False

    maximum = max(numbers)
    
    if len(numbers) < 2:
        # If only one element, there is no "second-to-last". 
        # Logically, comparing a single value against non-existent previous fails the condition conceptually,
        # but strictly speaking 'greater than' applies to two items. We'll return False for safety with n<2 unless specified otherwise.
        return False

    second_to_last = numbers[-2]
    
    return maximum > second_to_last

if __name__ == '__main__':
    # Sample test cases running without user input
    
    sample_1 = [3, 5, 7, 9]          # Max is 9, Second-to-last is 7. Expected: True
    sample_2 = [4, 8, 6, 8]          # Max is 8 (appears twice), Second-to-last is 6. Expected: True
    sample_3 = [10]                   # Only one element. No second-to-last. Expected: False based on logic above
    sample_4 = []                     # Empty list. Expected: False
    
    results_tests = {
        "Test 1 (Max > SecToLast):", 
        is_max_greater_than_second_to_last(sample_1), 
        ("Expected True") if not is_max_greater_than_second_to_last(sample_1) else ("Matched!")
    }

    print("Running sample tests...")
    
    # Execute checks against expected outcomes defined in comments above
    
    assert is_max_greater_than_second_to_last([3, 5, 7, 9]) == True, "Test 1 failed"
    assert is_max_greater_than_second_to_last([4, 8, 6, 8]) == True, "Test 2 failed"