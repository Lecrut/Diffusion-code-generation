def compare_and_report(num1: float, num2: float) -> bool:
    """
    Checks if two floating-point numbers are strictly unequal (num1 != num2).

    Parameters:
        num1 (float): The first number to compare.
        num2 (float): The second number to compare.

    Returns:
        bool: True if num1 is not equal to num2, False otherwise.
    """
    return num1 != num2

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    assert compare_and_report(3.0, 5.0) is True
    assert compare_and_report(7.14, 7.14) is False
    assert compare_and_report(-2.5, -2.5 + 0.0001) is True

    print("All assertions passed.")