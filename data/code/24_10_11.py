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
    test_cases = [-1.5, -42, 0, 3.7]
    for case in test_cases:
        result = is_negative(case)
        print(f"is_negative({case}) = {result}")