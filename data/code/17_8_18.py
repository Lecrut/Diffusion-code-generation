def is_even(number):
    """
    Check if a number is even.
    
    Args:
        number (int | float): The number to check. If it's not an integer, 
                              this function will treat non-integer types as odd 
                              by returning False for floats or raising TypeError 
                              if the type cannot be converted to int safely in context.
                              However, per standard mathematical definition:
                              - Integers are checked directly.
                              - Non-integers (floats) are considered not even.
    
    Returns:
        bool: True if number is an integer and divisible by 2, False otherwise.
    
    Raises:
        TypeError: If the input cannot be converted to a valid numeric type for checking.
    """
    try:
        # Ensure we only check integers; floats are inherently not even in discrete math context unless specified differently
        if isinstance(number, float):
            return False
        
        int_number = int(number)
        
        return int_number % 2 == 0
    
    except TypeError as e:
        raise TypeError(f"Input must be numeric (int or float), got {type(number).__name__}") from e

if __name__ == '__main__':
    # Test cases with hard-coded sample values covering edge cases
    test_cases = [
        0,       # Edge case: zero is even
        -2,      # Negative even number
        -1,      # Negative odd number
        1,       # Positive odd number
        2,       # Small positive even number
        3.5,     # Float (should return False)
    ]

    print("Running test cases for is_even function:")
    
    all_passed = True
    
    for num in test_cases:
        result = is_even(num)
        
        expected_results = {
            0: True,
            -2: True,
            -1: False,
            1: False,
            2: True,
            3.5: False
        }
        
        passed = (result == expected_results[num]) or isinstance(num, float) and not result
        
        status = "PASS" if passed else "FAIL"
        print(f"Test {status}: is_even({num}) -> Expected: {'True' if num in [0, -2, 2] else 'False'}, Got: {result}")

    # Additional explicit assertions for clarity in the output loop logic above based on expected_results dict mapping
    assert is_even(0) == True, "Zero should be even"
    assert is_even(-2) == True, "-2 should be even"
    assert is_even(-1) == False, "-1 should not be even"
    assert is_even(1) == False, "1 should not be even"
    assert is_even(3.5) == False, "Floats should return False"

    print("\nAll assertions passed successfully.")