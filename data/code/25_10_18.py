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
    test_cases = [0, -1, 1, 0.0, -0.0, 3.5]
    
    for case in test_cases:
        result = is_zero(case)
        print(f"is_zero({case}) -> {result}")