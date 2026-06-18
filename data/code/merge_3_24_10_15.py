def is_negative(value):
    """
    Check if a numerical value is strictly less than zero.

    Args:
        value (int | float): The number to evaluate.

    Returns:
        bool: True if value < 0, False otherwise.
    """
    return value < 0

if __name__ == '__main__':
    test_cases = [
        (-5),          # Expected: True
        (0),           # Expected: False
        (3.14),        # Expected: False
        (-2e-10),      # Expected: True
        float('-inf'),# Expected: True
    ]

    for num in test_cases:
        result = is_negative(num)
        print(f"is_negative({num!r}) = {result}")