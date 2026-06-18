def is_larger(a: float, b: float) -> bool:
    """
    Determine if number 'a' is strictly larger than number 'b'.
    
    Uses a single built-in comparison operator to minimize computational steps.
    
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
        (10.5, 5),           # Expected: True
        (-3, -7),            # Expected: True
        (42, 42),            # Expected: False
        (float('inf'), float('-inf')),  # Expected: True
    ]

    for val_a, val_b in test_cases:
        result = is_larger(val_a, val_b)
        print(f"is_larger({val_a}, {val_b}) = {result}")