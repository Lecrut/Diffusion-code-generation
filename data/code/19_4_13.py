def evaluate_inequality(x, y):
    """
    Checks if x is less than or equal to y.
    
    Handles potential type errors gracefully by attempting conversion 
    to float and returning False on failure.
    
    Args:
        x (any): The first value to compare.
        y (any): The second value to compare.
        
    Returns:
        bool: True if x <= y, otherwise False.
    """
    try:
        # Attempt to convert inputs to float for numeric comparison
        num_x = float(x)
        num_y = float(y)
        return num_x <= num_y
    except (ValueError, TypeError):
        # Return False if conversion fails due to type errors or invalid values
        return False

if __name__ == '__main__':
    # Hard-coded sample tests without user input
    test_cases = [
        ((5, 10), True),      # Normal numeric comparison
        ((-3.5, -2.5), True),# Negative numbers
        ((7, 7), True),       # Equal values (<= includes equality)
        ((9, 4), False),      # x > y case
        (("a", "b"), False),  # String comparison via float conversion fails -> False
        ((10.5, None), False),# Type error handling for None
    ]

    print("Running evaluate_inequality tests...")
    all_passed = True
    
    for i, (x_val, y_val) in enumerate(test_cases):
        result = evaluate_inequality(x_val, y_val)
        expected = test_cases[i][1]
        
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i+1}: compare({x_val}, {y_val}) -> Expected: {expected}, Got: {result} [{status}]")
        
        if result != expected:
            all_passed = False

    # Final status message based on test results
    if all_passed:
        print("\nAll tests passed successfully.")
    else:
        print("\nSome tests failed. Please review the output above.")