def compare_and_report(num1: float, num2: float) -> bool:
    """
    Checks if two floating-point numbers are strictly unequal (num1 != num2).

    Args:
        num1 (float): The first number to compare.
        num2 (float): The second number to compare.

    Returns:
        bool: True if num1 is not equal to num2, False otherwise.
    """
    return num1 != num2

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    result_1 = compare_and_report(3.0, 5.0)   # Expected: True
    result_2 = compare_and_report(7.14, 7.14) # Expected: False

    print(f"compare_and_report(3.0, 5.0) = {result_1}")
    print(f"compare_and_report(7.14, 7.14) = {result_2}")