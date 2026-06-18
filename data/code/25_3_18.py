def check_zero(value):
    """
    Checks if a given value is zero.
    
    Args:
        value (int): The integer to check.
        
    Returns:
        bool: True if value is 0, False otherwise.
    """
    return value == 0

# Sample values for testing without user input or command-line arguments
sample_values = [0, -5, 10]

if __name__ == '__main__':
    # Iterate through sample values to demonstrate functionality
    for val in sample_values:
        is_zero = check_zero(val)
        
        if is_zero:
            print(f"The value {val} is zero.")
        else:
            print(f"The value {val} is not zero.")