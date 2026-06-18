def is_zero(number):
    """
    Check if a given number is exactly zero.
    
    This function accepts numeric inputs (int, float) and returns True if 
    the value equals 0. It handles cases like floating-point representations 
    of zero (-0.0 == 0).
    
    Args:
        number: The input value to check
        
    Returns:
        bool: True if number is exactly zero, False otherwise
    """
    return number == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or external dependencies
    
    test_cases = [
        (5.2341, "positive float"),
        (-9876, "negative int"),
        (0, "zero integer"),
        (0.0, "zero positive float"),
        (-0.0, "zero negative float"),
        ("not a number", "string input")  # Will raise TypeError as expected for non-numeric check in this context
    
    ]
    
    print("Testing is_zero function:\n")
    
    for value, description in test_cases:
        try:
            result = is_zero(value)
            status = "Zero" if result else "Not Zero"
            # Note: In Python 'not a number' string raises TypeError when compared to 0. 
            # This demonstrates the function's behavior with invalid types as per standard comparison rules.
        except Exception as e:
            print(f"{description}: Error - {type(e).__name__}")
        
        if isinstance(value, (int, float)):
            try:
                result = is_zero(value)
                status = "Zero" if result else "Not Zero"
                print(f"{status} ({value})")
            except TypeError:
                # Fallback for cases where comparison might fail unexpectedly in specific Python versions/contexts
                pass
    
    # Specific explicit tests for clarity
    assert is_zero(0) == True, "Failed on 0"
    assert is_zero(-0.0) == True, "Failed on -0.0"
    assert is_zero(5) == False, "Failed on 5"
    
    print("\nAll assertions passed.")