def is_even(number):
    """
    Returns True if 'number' is an even integer, otherwise False.
    
    Args:
        number (int or float): The number to check. Non-integers are treated as odd/False 
                               for this implementation's simplicity unless converted.
        
    Returns:
        bool: True if the number is even, False otherwise.
    """
    # Handle non-integer inputs by converting them; strictly speaking, only ints should be checked here
    try:
        num = int(number)
    except (ValueError, TypeError):
        return False
    
    return num % 2 == 0

if __name__ == '__main__':
    # Hard-coded test cases with expected outputs for edge cases and normal values
    test_cases = [
        (0, True),       # Zero is even
        (-4, True),      # Negative even number
        (-3, False),     # Negative odd number
        (2, True),       # Small positive even number
        (1, False),      # Small positive odd number
        (50, True),      # Larger positive even number
    ]

    for value, expected in test_cases:
        result = is_even(value)
        assert result == expected, f"Test failed for {value}: expected {expected}, got {result}"

    print("All tests passed successfully.")