def is_positive(number: float) -> bool:
    """
    Check if a number is strictly positive (greater than zero).

    Args:
        number (float): The numerical value to check.

    Returns:
        bool: True if the number is greater than 0, False otherwise.
    """
    return number > 0

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    samples = [1, -5, 0, 3.14, float('-inf'), float('inf')]

    for sample in samples:
        result = is_positive(sample)
        print(f"is_positive({sample}) = {result}")