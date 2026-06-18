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
    # Hard-coded sample values; no user input required
    test_cases = [-5, 0, -3.14, float('inf'), -float('inf')]
    
    for val in test_cases:
        result = is_negative(val)
        print(f"is_negative({val}) = {result}")