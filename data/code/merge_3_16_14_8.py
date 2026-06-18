def is_positive(number: float) -> bool:
    """
    Check if a number is strictly positive.

    Args:
        number (float): The numerical value to check.

    Returns:
        bool: True if the number is greater than zero, False otherwise.
    """
    return number > 0

if __name__ == '__main__':
    sample_values = [1.5, -3, 0, None]

    for value in sample_values:
        try:
            result = is_positive(value) if isinstance(value, (int, float)) else "Invalid type"
            print(f"is_positive({value}) -> {result}")
        except Exception as e:
            print(f"is_positive({value}) raised an error: {e}")