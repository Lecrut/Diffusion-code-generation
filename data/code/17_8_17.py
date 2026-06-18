"""
Module containing a function to check if a number is even.
Includes test cases demonstrating correctness against edge cases: zero, positive integers, and negative numbers.
No external dependencies or interactive input required.
"""

def is_even(number):
    """
    Returns True if the given integer is even, False otherwise.

    Args:
        number (int): The integer to check.

    Returns:
        bool: True if 'number' is divisible by 2, False otherwise.
    """
    return number % 2 == 0

if __name__ == '__main__':
    # Test cases with hard-coded sample values covering edge cases
    
    test_cases = [
        (0, True),       # Edge case: zero
        (1, False),      # Positive odd number
        (-5, False),     # Negative odd number
        (2, True),       # Small positive even number
        (-4, True),      # Negative even number
    ]

    for input_val, expected_result in test_cases:
        actual_result = is_even(input_val)
        
        if actual_result == expected_result:
            print(f"Test passed: is_even({input_val}) returned {actual_result}")
        else:
            print(f"Test failed: is_even({input_val}) returned {actual_result}, expected {expected_result}")

    # Run a quick sanity check on the main function logic directly to ensure it prints at least one success message before exit.
    assert is_even(10) == True, "Sanity check for positive even number failed."
    print("All tests and sanity checks completed successfully.")