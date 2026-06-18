def is_negative(value: float) -> bool:
    """
    Returns True if value is strictly less than zero, False otherwise.
    
    Args:
        value (float): The numerical argument to check.
        
    Returns:
        bool: True if value < 0, else False.
    """
    return value < 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        -5.0,   # Should be True
        0.0,    # Should be False (zero is not negative)
        -1e-20,# Very small negative number -> should be True
        float('inf'),# Positive infinity -> should be False
        float('-inf'),# Negative infinity -> should be True
        3.14,   # Positive float -> should be False
    ]

    for test_val in test_cases:
        result = is_negative(test_val)
        print(f"is_negative({test_val}) = {result}")