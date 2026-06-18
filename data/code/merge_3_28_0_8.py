def is_larger(a: int | float, b: int | float) -> bool:
    """
    Returns True if 'a' is strictly larger than 'b', otherwise False.
    
    Args:
        a (int or float): The first number to compare.
        b (int or float): The second number to compare.
        
    Returns:
        bool: True if a > b, else False.
    """
    return a > b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    test_cases = [
        (10, 5),      # Expected: True
        (3.14, 2.71), # Expected: True
        (-1, -2),     # Expected: True
        (0, 0),       # Expected: False
        (5, 10),      # Expected: False
    ]

    for val_a, val_b in test_cases:
        result = is_larger(val_a, val_b)
        print(f"is_larger({val_a!r}, {val_b!r}) -> {result}")