def is_larger(a: float, b: float) -> bool:
    """
    Returns True if a is strictly larger than b, otherwise False.
    
    Args:
        a (float): The first number to compare.
        b (float): The second number to compare.
        
    Returns:
        bool: True if a > b, else False.
    """
    return a > b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        (5.0, 3.0),   # Expected: True
        (10, 20),     # Expected: False
        (-1.5, -2.7),# Expected: True
        (42, 42),     # Expected: False
    ]

    for val_a, val_b in test_cases:
        result = is_larger(val_a, val_b)
        print(f"is_larger({val_a}, {val_b}) = {result}")