def compare_and_report(num1: float, num2: float) -> bool:
    """
    Checks if two numbers are strictly unequal (num1 != num2).

    Args:
        num1 (float): The first numeric value to compare.
        num2 (float): The second numeric value to compare.

    Returns:
        bool: True if num1 is not equal to num2, False otherwise.
    """
    return num1 != num2

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    result_1 = compare_and_report(5.0, 3.7)
    print(f"compare_and_report(5.0, 3.7) -> {result_1}")

    result_2 = compare_and_report(4.2, 4.2)
    print(f"compare_and_report(4.2, 4.2) -> {result_2}")

    result_3 = compare_and_report(-10.5, -10.5 + 0.001)
    print(f"compare_and_report({-10.5}, {-10.5 + 0.001}) -> {result_3}")