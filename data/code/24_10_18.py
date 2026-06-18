def is_negative(value: float) -> bool:
    """
    Check if a number is strictly less than zero.

    Args:
        value (float): A numerical argument to evaluate.

    Returns:
        bool: True if the number is negative, False otherwise.
    """
    return value < 0

if __name__ == '__main__':
    # Hard-coded sample values to verify functionality without user input or external dependencies
    test_cases = [10, -5.5, 0, float('inf'), float('-inf')]

    for num in test_cases:
        result = is_negative(num)
        print(f"is_negative({num}) = {result}")