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
    # Sample test cases with hard-coded values
    tests = [
        (5.0, 3.0),   # Expected: True
        (1.0, 2.0),   # Expected: False
        (-5.0, -3.0),# Expected: False
        (float('inf'), float('-inf')), # Expected: True
    ]

    for i in range(0, len(tests), 2):
        a = tests[i]
        b = tests[i + 1]
        
        result = is_larger(a, b)
        
        if isinstance(result, bool):
            print(f"is_larger({a}, {b}) -> {result}")
        else:
            print(f"Error in test case ({a}, {b}): expected boolean")