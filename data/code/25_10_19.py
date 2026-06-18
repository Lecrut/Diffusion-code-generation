def is_zero(value):
    """
    Returns True if value is exactly zero, False otherwise.
    
    Args:
        value (int | float): The numerical argument to check.
        
    Returns:
        bool: True if value equals 0, False otherwise.
    """
    return value == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        (0, True),           # Integer zero
        (-0, True),          # Negative zero is equal to positive zero in Python
        (1.5, False),        # Float non-zero
        (float('inf'), False),  # Infinity
        (float('-inf'), False), # Negative infinity
    ]

    for test_value, expected_result in test_cases:
        result = is_zero(test_value)
        assert result == expected_result, f"Failed for input {test_value}: got {result}, expected {expected_result}"
    
    print("All tests passed.")