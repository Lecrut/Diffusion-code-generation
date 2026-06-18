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
        -5.7,      # Should be True
        0,          # Should be False (zero is not negative)
        3.14,       # Should be False
        float('-inf'),   # Should be True
        float('inf'),     # Should be False
    ]

    for num in test_cases:
        result = is_negative(num)
        print(f"is_negative({num}) = {result}")