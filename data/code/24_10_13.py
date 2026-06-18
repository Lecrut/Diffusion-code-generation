def is_negative(value):
    """
    Returns True if value is strictly less than zero, False otherwise.

    Args:
        value (int | float): A numerical argument to evaluate.

    Returns:
        bool: Result indicating whether the number is negative.
    
    Note:
        This function assumes 'value' is a valid numeric type. Non-numeric inputs 
        will raise an appropriate TypeError as Python handles such cases natively 
        in comparisons without explicit handling here for robustness and clarity.

    Raises:
        TypeError: If value cannot be compared to zero (e.g., string).
    """
    return value < 0

if __name__ == '__main__':
    # Hard-coded sample values testing various numeric scenarios
    test_cases = [
        (-5, True),       # Negative integer
        (-3.14, True),   # Negative float
        (0, False),       # Zero is not negative
        (0.0, False),     # Positive zero as float
        (10, False),      # Positive integer
        (2e-5, False),    # Small positive float in scientific notation
        (-1e3, True),     # Large negative float in scientific notation
    ]

    for num, expected in test_cases:
        result = is_negative(num)
        if result != expected:
            print(f"ERROR: is_negative({num}) returned {result}, expected {expected}")
        else:
            print(f"is_negative({num!r}: OK)")