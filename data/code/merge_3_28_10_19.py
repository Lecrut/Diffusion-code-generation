def is_larger(a: float, b: float) -> bool:
    """
    Returns True if a is strictly greater than b, False otherwise.
    
    Args:
        a (float): The first numerical value to compare.
        b (float): The second numerical value to compare.
        
    Returns:
        bool: True if a > b, else False.
    """
    return a > b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        (10, 5),      # Expected: True
        (3.14, 2.71),# Expected: True
        (-1, -5),     # Expected: False
        (0, 0),       # Expected: False
        (float('inf'), float('-inf')), # Expected: True
    ]

    for val_a, val_b in test_cases:
        result = is_larger(val_a, val_b)
        print(f"is_larger({val_a}, {val_b}) = {result}")