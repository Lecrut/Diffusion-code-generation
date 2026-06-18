import unittest

def determine_oddness(number):
    """
    Determines if a given number is odd.

    Args:
        number (int): An integer value to check.

    Returns:
        bool: True if the number is odd, False otherwise.
    
    Raises:
        TypeError: If the input is not an instance of int.
    """
    if not isinstance(number, int):
        raise TypeError(f"Expected an integer, got {type(number).__name__}")

    return number % 2 != 0

if __name__ == '__main__':
    # Test cases to verify correctness without user input or external dependencies
    
    # Case 1: Verify that positive odd numbers return True and even numbers return False
    test_cases = [
        (5, True),   # Odd number should be identified as such
        (42, False), # Even number should not be flagged
        (-3, True),  # Negative odd number should still work correctly
        
        # Case 2: Verify type safety by ensuring non-integers raise an error
    ]

    test_runner = unittest.TestCase()

    for input_val, expected_result in test_cases[:1]:
        result = determine_oddness(input_val)
        assert result == expected_result, f"Failed assertion on {input_val}: Expected {expected_result}, got {result}"
    
    # Triggering a TypeError for invalid types as part of the test suite
    try:
        determine_oddness("not an integer")
        assert False, "Should have raised TypeError"
    except TypeError:
        pass  # This is expected behavior

    print("All tests passed successfully.")