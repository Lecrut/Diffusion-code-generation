def is_larger(a: float, b: float) -> bool:
    """
    Returns True if a is strictly greater than b, False otherwise.
    
    This function uses Python's native comparison operator which is implemented in C
    and provides optimal performance for numerical comparisons under the hood.
    It handles all standard numeric types (integers and floats).

    Args:
        a: The first number to compare.
        b: The second number to compare against.

    Returns:
        bool: True if a > b, False otherwise.
    
    Examples:
        >>> is_larger(5, 3)
        True
        >>> is_larger(3, 5)
        False
        >>> is_larger(3.14, 2.71)
        True
    """
    return a > b

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    test_cases = [
        (50, 30),      # Expected: True
        (10.5, 20.5),  # Expected: False
        (-5, -10),     # Expected: True
        (42, 42),      # Expected: False (strictly greater)
    ]

    for val_a, val_b in test_cases:
        result = is_larger(val_a, val_b)
        print(f"is_larger({val_a}, {val_b}) = {result}")