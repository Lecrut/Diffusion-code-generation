def is_larger(a: float, b: float) -> bool:
    """
    Determine if number 'a' is larger than number 'b'.
    
    Uses built-in comparison operators to minimize computational steps.
    
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
        (10.5, 2),
        (-3, -7),
        (42, 99),
        (float('inf'), float('-inf')),
        (0.0, 0.0)
    ]

    for val_a, val_b in test_cases:
        result = is_larger(val_a, val_b)
        print(f"is_larger({val_a}, {val_b}) = {result}")