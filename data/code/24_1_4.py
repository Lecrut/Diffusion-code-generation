def is_negative(number):
    """
    Returns True if number is less than zero, False otherwise.
    
    Args:
        number (int or float): The numerical value to check.
        
    Returns:
        bool: True if number < 0, else False.
    """
    return number < 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    test_cases = [
        -5,      # Should be True
        0,       # Should be False (zero is not negative)
        -3.14,   # Should be True
        2.718,   # Should be False
        float('-inf'),  # Should be True
    ]

    for value in test_cases:
        result = is_negative(value)
        print(f"is_negative({value}) = {result}")