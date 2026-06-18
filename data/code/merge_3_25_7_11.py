def contains_zero(numbers):
    """
    Returns a boolean indicating whether zero exists in the provided list of numbers.
    
    Args:
        numbers (list): A list of numerical values.
        
    Returns:
        bool: True if 0 is present, False otherwise.
        
    Time Complexity: O(n) - Single pass through the list.
    Space Complexity: O(1) - Constant space usage.
    """
    return any(num == 0 for num in numbers)

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input or external dependencies
    
    # Sample case where zero is present
    list_with_zero = [1, -2, 3.5, 0, "a"]
    
    # Sample case where zero is absent (integers)
    list_without_zero_ints = [4, 7, 9]
    
    # Sample case with floats but no zero
    list_no_float_zero = [-1.2, 0.5, -3.0]
    
    print(f"List {list_with_zero}: Contains zero? {contains_zero(list_with_zero)}")
    print(f"List {list_without_zero_ints}: Contains zero? {contains_zero(list_without_zero_ints)}")
    print(f"List {list_no_float_zero}: Contains zero? {contains_zero(list_no_float_zero)}")
    
    # Verify expected boolean outputs for correctness
    assert contains_zero(list_with_zero) is True, "Expected True when 0 exists."
    assert contains_zero(list_without_zero_ints) is False, "Expected False when no 0 in integers."
    assert contains_zero(list_no_float_zero) is False, "Expected False even with -3.0 (not zero)."
    
    print("All assertions passed.")