def is_greater(a: float, b: float) -> bool:
    """
    Returns True if a > b, otherwise False.
    
    This function uses Python's native comparison operator which 
    is implemented in C and offers optimal performance for numerical comparisons.
    
    Args:
        a (float): The first number to compare.
        b (float): The second number to compare.
        
    Returns:
        bool: True if a is greater than b, False otherwise.
    """
    return a > b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        (10.5, 5),       # Expected: True
        (-3, -7),        # Expected: False
        (42, 42),        # Expected: False (equal)
        (float('inf'), float('-inf')), # Expected: True
    ]

    for val_a, val_b in test_cases:
        result = is_greater(val_a, val_b)
        print(f"is_greater({val_a}, {val_b}) = {result}")