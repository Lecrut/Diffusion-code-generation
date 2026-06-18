def evaluate_inequality(x, y):
    """
    Checks if x is less than or equal to y.
    
    Args:
        x (any comparable type): The first value to compare.
        y (any comparable type): The second value to compare.
        
    Returns:
        bool: True if x <= y, False otherwise.
        
    Raises:
        TypeError: If either x or y cannot be compared using '<=' operator.
    
    Note: This function does not include try-except for TypeError as per strict comparison logic requirements in Python 
          unless the prompt specifically asks to handle type errors gracefully by catching them and returning False/None.
          However, re-reading the task: "handle potential type errors gracefully".
          Therefore, we will wrap the comparison in a try-except block where it catches TypeError exceptions and return False.
    """
    try:
        return x <= y
    except (TypeError, AttributeError):
        # Gracefully handle cases where types cannot be compared or are not comparable objects
        return False

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    
    # Test 1: Integer comparison (True case)
    result1 = evaluate_inequality(3, 5)
    print(f"evaluate_inequality(3, 5) -> {result1}")
    
    # Test 2: Float comparison (False case)
    result2 = evaluate_inequality(4.9, 4.8)
    print(f"evaluate_inequality(4.9, 4.8) -> {result2}")
    
    # Test 3: Mixed integer and float (True case if equal or less)
    result3 = evaluate_inequality(5, 5.0)
    print(f"evaluate_inequality(5, 5.0) -> {result3}")
    
    # Test 4: String comparison (False case - 'b' > 'a')
    result4 = evaluate_inequality('b', 'a')
    print(f"evaluate_inequality('b', 'a') -> {result4}")
    
    # Test 5: Comparison with non-numeric types to test graceful error handling
    try:
        result5 = evaluate_inequality("hello", [1, 2])
        print(f"evaluate_inequality(\"hello\", [1, 2]) -> {result5} (Handled gracefully)")
    except Exception as e:
        # Should not happen with the implementation defined in evaluate_inequality 
        # unless there's a specific TypeError that wasn't covered by generic handling logic.
        print(f"Unexpected error for 'hello' vs list: {e}")

    # Test 6: None comparison (Graceful fallback)
    result6 = evaluate_inequality(None, "string")
    print(f"evaluate_inequality(None, 'string') -> {result6} (Handled gracefully)")