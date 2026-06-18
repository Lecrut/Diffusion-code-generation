def is_negative(value):
    """
    Check if a number is strictly less than zero.

    Args:
        value (int | float): The numerical argument to evaluate.

    Returns:
        bool: True if value < 0, False otherwise.
    
    Note: This function handles all numeric types including integers and floats.
          It does not perform type conversion; non-numeric inputs will raise a TypeError.
    """
    return value < 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        (-5, True),      # Negative integer -> True
        (0, False),       # Zero is not negative -> False
        (3.14, False),    # Positive float -> False
        (-2.7e-3, True),  # Small negative float -> True
        (float('-inf'), True),   # Negative infinity -> True
        (float('inf'), False),   # Infinity is not less than zero -> False
    ]

    for num, expected in test_cases:
        result = is_negative(num)
        status = "✓" if result == expected else "✗"
        print(f"{status} is_negative({num!r}) = {result} (expected {expected})")