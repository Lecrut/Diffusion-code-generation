import math

# Predefined threshold value used by the check function
THRESHOLD = 10.5

def is_above_threshold(value: float) -> bool:
    """
    Check if a given numeric value is strictly greater than the predefined THRESHOLD.

    Args:
        value (float): The number to evaluate against the threshold.

    Returns:
        bool: True if value > THRESHOLD, otherwise False.
    """
    return value > THRESHOLD

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or network access
    
    test_cases = [
        (50.0, True),      # 50 is greater than 10.5
        (10.5, False),     # Equal to threshold should return False
        (-2.3, False),     # Negative number less than threshold
        (9.99, False),     # Just below threshold
        (float('inf'), True)   # Infinity is greater than any finite number
    ]

    for value, expected in test_cases:
        result = is_above_threshold(value)
        assert result == expected, f"Test failed for {value}: expected {expected}, got {result}"

    print("All tests passed.")