def is_strictly_greater(a: float, b: float) -> bool:
    """
    Check if number 'a' is strictly greater than number 'b'.
    
    Args:
        a (float): The first number to compare.
        b (float): The second number to compare.
        
    Returns:
        bool: True if a > b, False otherwise.
    """
    try:
        return float(a) > float(b)
    except (ValueError, TypeError):
        # Gracefully handle cases where inputs cannot be converted to floats
        raise ValueError("Both arguments must be convertible to numbers.")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        (10, 5),       # Expected: True
        (3.14, 2.71),  # Expected: True
        (-1, -5),      # Expected: True
        (7, 7),         # Expected: False (strictly greater)
        ("8", "9"),     # String inputs that can be converted to numbers; Expected: False
    ]

    for i, (val_a, val_b) in enumerate(test_cases):
        try:
            result = is_strictly_greater(val_a, val_b)
            print(f"Test case {i + 1}: {isinstance(val_a, str)} vs {isinstance(val_b, str)}")
            print(f"is_strictly_greater({val_a}, {val_b}) = {result}")
        except ValueError as e:
            print(f"Error in test case {i + 1}: {e}")

    # Additional explicit numeric tests to ensure robustness