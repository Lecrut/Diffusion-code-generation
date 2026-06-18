def is_even(number: int) -> bool:
    """
    Check if a given integer is even.

    Args:
        number (int): The integer to check.

    Returns:
        bool: True if the number is even, False otherwise.
    """
    return number % 2 == 0

if __name__ == '__main__':
    # Test cases with hard-coded sample values covering edge cases
    
    test_cases = [
        (0, True),      # Zero case
        (-4, True),     # Negative even number
        (5, False),     # Positive odd number
        (-3, False),    # Negative odd number
        (10**9 - 2, True),   # Large positive even number
        -(10**9 + 10),      # Large negative even number
    ]

    print("Running is_even tests...")
    
    for test_input, expected_output in test_cases:
        result = is_even(test_input)
        status = "PASS" if result == expected_output else "FAIL"
        
        # Print detailed output only on failure to keep clean console by default, 
        # but here we print all results as per standard testing practice for verification.
        print(f"is_even({test_input})")
        print(f"  Expected: {expected_output}, Got: {result} -> [{status}]")

    # Verify if all tests passed (optional assertion block)
    assert len(test_cases), "No test cases defined."
    
    for test_input, expected in test_cases:
        assert is_even(test_input) == expected, f"Test failed for input {test_input}"
        
    print("\nAll tests completed successfully.")