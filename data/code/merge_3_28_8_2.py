def compare_and_report(num1: float, num2: float) -> bool:
    """
    Performs a strict inequality check between two floating-point numbers.

    Args:
        num1 (float): The first number to compare.
        num2 (float): The second number to compare.

    Returns:
        bool: True if num1 is strictly less than num2, False otherwise.
    """
    return num1 < num2

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    result_1 = compare_and_report(3.5, 7.0)
    print(f"compare_and_report(3.5, 7.0) = {result_1}")

    result_2 = compare_and_report(-10.0, -5.0)
    print(f"compare_and_report(-10.0, -5.0) = {result_2}")

    result_3 = compare_and_report(4.2, 4.2)
    print(f"compare_and_report(4.2, 4.2) = {result_3}")

    result_4 = compare_and_report(1e-5, 0.0001)
    print(f"compare_and_report(1e-5, 0.0001) = {result_4}")