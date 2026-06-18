def is_negative(number: float) -> bool:
    """
    Returns True if the number is less than zero, False otherwise.
    
    Args:
        number (float): The numerical value to check.
        
    Returns:
        bool: True if number < 0, else False.
    """
    return number < 0

if __name__ == '__main__':
    # Sample test cases run without user input or external dependencies
    test_values = [-5.2, -1, 0, 3.7]
    
    for val in test_values:
        result = is_negative(val)
        print(f"is_negative({val}) = {result}")