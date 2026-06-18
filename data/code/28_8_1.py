def compare_and_report(num1: float, num2: float) -> bool:
    """
    Checks if two floating-point numbers are strictly unequal (num1 != num2).

    Args:
        num1 (float): The first numeric value to compare.
        num2 (float): The second numeric value to compare.

    Returns:
        bool: True if num1 is not equal to num2, False otherwise.
    
    Example:
        >>> compare_and_report(3.0, 4.5)
        True
        >>> compare_and_report(7.0, 7.0)
        False
    """
    return num1 != num2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_a: float = 5.5
    sample_b: float = 3.0
    
    result: bool = compare_and_report(sample_a, sample_b)
    
    if result:
        print(f"{sample_a} is strictly greater than {sample_b}")
    else:
        print(f"{sample_a} equals or matches {sample_b}")