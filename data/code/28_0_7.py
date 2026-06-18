def is_larger(a: float, b: float) -> bool:
    """
    Returns True if a is strictly larger than b, otherwise False.
    
    Parameters:
        a (float): The first number to compare.
        b (float): The second number to compare.
        
    Returns:
        bool: True if a > b, else False.
    """
    return a > b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        (10, 5),      # Expected: True
        (3.14, 2.71),# Expected: True
        (-1, -5),     # Expected: True
        (0, 0),       # Expected: False
        (float('inf'), float('-inf')), # Expected: True
    ]

    for a, b in test_cases:
        result = is_larger(a, b)
        print(f"is_larger({a}, {b}) = {result}")