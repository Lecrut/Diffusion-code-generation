def check_all_positive(numbers):
    """
    Checks if all numbers in the list are positive (greater than 0).
    
    Args:
        numbers (list): A list of numerical values.
        
    Returns:
        bool: True if all elements are strictly greater than zero, False otherwise.
             Immediately returns upon finding a non-positive value for efficiency.
    """
    for num in numbers:
        if num <= 0:
            return False
    return True

if __name__ == '__main__':
    # Sample test cases hard-coded as per requirements
    
    # Test case 1: All positive integers and floats
    all_positive = [1, 2.5, 3]
    
    # Test case 2: Contains zero
    contains_zero = [10, 0, 20]
    
    # Test case 3: Contains negative number
    has_negative = [-5, -1, 4]
    
    # Test case 4: Empty list (vacuously true)
    empty_list = []
    
    print(f"Test Case 1 ({all_positive}): {check_all_positive(all_positive)}")      # Expected: True
    print(f"Test Case 2 ({contains_zero}): {check_all_positive(contains_zero)}")   # Expected: False
    print(f"Test Case 3 ({has_negative}): {check_all_positive(has_negative)}")  # Expected: False
    print(f"Test Case 4 ({empty_list}): {check_all_positive(empty_list)}")      # Expected: True
    
    assert check_all_positive(all_positive) == True, "All positive case failed"
    assert check_all_positive(contains_zero) == False, "Zero presence case failed"
    assert check_all_positive(has_negative) == False, "Negative number case failed"
    assert check_all_positive(empty_list) == True, "Empty list case failed"
    
    print("All assertions passed.")