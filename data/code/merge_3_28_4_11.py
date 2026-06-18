def is_larger(num1: float, num2: float) -> bool:
    """
    Determines if num1 is strictly larger than num2 using built-in comparison.
    This function performs a single computational step (one comparison).
    
    Args:
        num1: The first number to compare.
        num2: The second number to compare.
        
    Returns:
        True if num1 > num2, False otherwise.
    """
    return num1 > num2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    test_cases = [
        (50.5, 49.8),   # Expected: True
        (3.14, 3.15),   # Expected: False
        (-10, -20),     # Expected: True
        (1e-5, 1e-6),   # Expected: True
    ]

    print("Testing is_larger function:")
    for val1, val2 in test_cases:
        result = is_larger(val1, val2)
        status = "PASS" if result else (f"FALSED (Expected False)" if not val1 > val2 else f"PASSED")
        print(f"is_larger({val1}, {val2}) -> {result}")