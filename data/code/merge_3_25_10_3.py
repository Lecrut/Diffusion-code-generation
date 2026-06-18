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
        (0, True),
        (-1e-324, False),  # Smallest positive float in some systems; negative is not zero
        (float('inf'), False),
        (float('-inf'), False),
        (0.0, True),       # Explicitly zero as float
        (int(0), True),    # Zero as int
        (-1e-324 + 1e-324, True),  # Result of cancellation to exactly zero
        (float('nan'), False),
    ]

    for test_value, expected in test_cases:
        result = is_zero(test_value)
        assert result == expected, f"Failed for input {test_value}: got {result}, expected {expected}"
    
    print("All tests passed.")