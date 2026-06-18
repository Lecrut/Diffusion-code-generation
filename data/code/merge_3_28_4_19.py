def is_larger(a: float, b: float) -> bool:
    """
    Determines if number 'a' is larger than number 'b'.
    
    Uses Python's built-in comparison operator '>' which handles all numeric types efficiently.
    This approach minimizes computational steps by avoiding explicit conditional logic or custom implementations.
    
    Args:
        a (float): The first number to compare.
        b (float): The second number to compare.
        
    Returns:
        bool: True if 'a' is strictly greater than 'b', False otherwise.
    """
    return a > b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        (10, 5),      # Expected: True
        (-3, -7),     # Expected: True
        (4.2, 4.2),   # Expected: False (equal)
        (float('inf'), float('-inf')), # Expected: True
    ]

    for num1, num2 in test_cases:
        result = is_larger(num1, num2)
        print(f"is_larger({num1}, {num2}) -> {result}")