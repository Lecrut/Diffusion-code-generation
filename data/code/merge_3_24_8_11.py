def check_negative(value):
    """
    Checks if a given integer is negative.
    
    Args:
        value (int): The integer to check.
        
    Returns:
        bool: True if the number is less than zero, False otherwise.
    """
    return value < 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    test_values = [-5, 10, -3]

    for num in test_values:
        is_negative = check_negative(num)
        
        if is_negative:
            print(f"The number {num} is negative.")
        else:
            print(f"The number {num} is not negative.")