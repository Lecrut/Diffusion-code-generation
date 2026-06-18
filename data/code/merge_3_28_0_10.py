def is_larger(a: float, b: float) -> bool:
    """
    Returns True if a is strictly larger than b, False otherwise.
    
    Args:
        a (float): The first number to compare.
        b (float): The second number to compare.
        
    Returns:
        bool: True if a > b, False otherwise.
    """
    return a > b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        (5, 3),      # Expected: True
        (10, 10),    # Expected: False (equal)
        (-2.5, -3.7)# Expected: True
    ]

    for val_a, val_b in test_cases:
        result = is_larger(val_a, val_b)
        print(f"is_larger({val_a}, {val_b}) = {result}")