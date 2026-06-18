def compare_and_report(num1: float, num2: float) -> bool:
    """
    Checks if two floating-point numbers are strictly unequal (num1 != num2).

    Args:
        num1 (float): The first numeric value.
        num2 (float): The second numeric value.

    Returns:
        bool: True if num1 is not equal to num2, False otherwise.
    """
    return num1 != num2

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    result_1 = compare_and_report(3.5, 4.0)
    print(f"compare_and_report(3.5, 4.0) -> {result_1}")

    result_2 = compare_and_report(7.89, 7.89)
    print(f"compare_and_report(7.89, 7.89) -> {result_2}")

    result_3 = compare_and_report(-0.5, -0.1)
    print(f"compare_and_report(-0.5, -0.1) -> {result_3}")