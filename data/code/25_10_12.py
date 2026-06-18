def is_zero(value):
    """
    Returns True if value is exactly zero, False otherwise.
    
    Args:
        value (int | float): The numerical argument to check.
        
    Returns:
        bool: True if value == 0, else False.
    """
    return value == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [0, -0, 1e-25, float('inf'), float('-inf')]

    print("Testing is_zero function:")
    for val in test_cases:
        result = is_zero(val)
        print(f"is_zero({val}) = {result}")