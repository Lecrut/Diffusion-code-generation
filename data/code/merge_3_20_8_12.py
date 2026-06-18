def check_equal(values):
    """
    Checks if two values are equal based on both their value AND type.
    
    Args:
        values (list): A list containing exactly two elements to compare.
        
    Returns:
        bool: True if the types and values match, False otherwise.
    """
    val1 = values[0]
    val2 = values[1]
    
    # Direct comparison of type objects ensures exact type matching (e.g., int vs float)
    is_same_type = type(val1) == type(val2)
    
    # Value equality check
    are_values_equal = val1 == val2
    
    return is_same_type and are_values_equal

if __name__ == '__main__':
    # Hard-coded sample values to avoid any user input, prompts, or external dependencies.
    # Example 1: Two integers with the same value (should be True)
    test_case_1 = [5, 5]
    
    # Example 2: Integers with different values (should be False)
    test_case_2 = [3, 7]
    
    # Example 3: Integer and Float representing the same numerical value 
    # but having different types (should be False due to type mismatch)
    test_case_3 = [5.0, 5]

    print(f"Test Case 1 ({test_case_1}): {check_equal(test_case_1)}")
    print(f"Test Case 2 ({test_case_2}): {check_equal(test_case_2)}")
    print(f"Test Case 3 ({test_case_3}): {check_equal(test_case_3)}")