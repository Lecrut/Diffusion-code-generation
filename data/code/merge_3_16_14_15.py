def is_positive(number: float) -> bool:
    """
    Check if a number is strictly positive.

    Args:
        number (float): The numerical value to check. It can be an integer or float.

    Returns:
        bool: True if the number is greater than zero, False otherwise.
    
    Examples:
        >>> is_positive(5)
        True
        >>> is_positive(-3.14)
        False
        >>> is_positive(0)
        False
        >>> is_positive(float('inf'))
        True
    """
    return number > 0

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    samples = [5, -10.5, 0, float('inf'), None]

    for sample in samples:
        if isinstance(sample, (int, float)):
            result = is_positive(sample)
            print(f"is_positive({sample}) = {result}")
        else:
            # Handle non-numeric types gracefully without raising an error that stops execution
            try:
                numeric_value = sample  # Just for type checking in loop logic if needed, but we cast above to check isinstance
                result = is_positive(sample)
                print(f"is_positive({sample}) = {result}")
            except (TypeError, ValueError):
                print(f"Warning: Cannot determine positivity for non-numeric value '{sample}'")