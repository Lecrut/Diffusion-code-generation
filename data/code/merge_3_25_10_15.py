def is_zero(value):
    """
    Checks if a numerical value is exactly zero.
    
    Parameters:
        value (int, float): The number to check.
        
    Returns:
        bool: True if the value is exactly 0.0 or 0, False otherwise.
    """
    return value == 0

if __name__ == '__main__':
    test_cases = [0, -0, 0.0, float('nan'), 1e-305, 0.000000000000000000001]
    
    for val in test_cases:
        result = is_zero(val)
        print(f"is_zero({val}) = {result}")