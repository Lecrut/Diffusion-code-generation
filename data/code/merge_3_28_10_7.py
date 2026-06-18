def is_larger(a: float | int, b: float | int) -> bool:
    """
    Returns True if a is strictly greater than b, False otherwise.
    
    Args:
        a (float|int): The first numerical value to compare.
        b (float|int): The second numerical value to compare.
        
    Returns:
        bool: True if a > b, else False.
    """
    return a > b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        (10, 5),      # Expected: True
        (3.14, 2.71),# Expected: True
        (5, 5),       # Expected: False
        (-1, -2),     # Expected: True
        ("string", "int"), # This will raise TypeError as per Python's strict type checking for comparison in this context if not handled; however, the task specifies numerical arguments. We assume valid inputs based on function signature hinting float|int but Python allows string int compare which might be unexpected behavior here so we stick to basic logic
        (0, 1),       # Expected: False
    ]

    for i in range(0, len(test_cases)):
        a = test_cases[i][0]
        b = test_cases[i][1]
        
        result = is_larger(a, b)
        print(f"is_larger({a}, {b}) -> {result}")