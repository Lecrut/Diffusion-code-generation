"""
Module to check if a number is strictly positive.
"""

def is_positive(number: float) -> bool:
    """
    Returns True if the given number is strictly positive, False otherwise.

    Args:
        number (float): A numerical value to evaluate.

    Returns:
        bool: True if number > 0, False otherwise.
    """
    return number > 0

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_values = [5.2, -3, 0, 1e-9, float('-inf'), float('inf')]

    for value in sample_values:
        result = is_positive(value)
        print(f"is_positive({value}) = {result}")