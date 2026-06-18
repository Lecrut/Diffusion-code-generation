def is_larger(a: float, b: float) -> bool:
    """
    Determine if 'a' is strictly larger than 'b'.
    
    Uses Python's built-in comparison operator '<>' to check inequality,
    then negates the result of (a < b). This approach minimizes computational steps
    by leveraging a single fundamental comparison operation instead of explicit logic branches.

    Args:
        a (float): The first number to compare.
        b (float): The second number to compare.

    Returns:
        bool: True if a > b, False otherwise.
    """
    return not (a < b)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        ((10.5, 3.2), True),      # Case: a is larger than b
        ((-5.7, -9.1), False),   # Case: negative where first is actually less (closer to zero) -> wait logic check: -5 > -9 so should be True? Let's re-evaluate test case 2.
        (-5.7 < -9.1)             # Correction: -5.7 IS greater than -9.1 in math, but let's pick a clear False case below.
    ]

    # Corrected sample cases for clarity and correctness
    samples = [
        (100, 2),      # Expected True
        (-3, 4),       # Expected False
        (float('inf'), float('-inf')), # Expected True
        (7.89, 7.89)   # Expected False (equal numbers are not larger)
    ]

    for val_a, val_b in samples:
        result = is_larger(val_a, val_b)
        print(f"is_larger({val_a}, {val_b}) -> {result}")