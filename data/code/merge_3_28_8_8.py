def compare_and_report(num1: float, num2: float) -> bool:
    """
    Strictly checks if num1 is greater than num2 without modifying either operand.

    Args:
        num1 (float): The first numerical value to compare.
        num2 (float): The second numerical value to compare.

    Returns:
        bool: True if num1 > num2, False otherwise.
    """
    return num1 > num2

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    result_a = compare_and_report(5.0, 3.0)   # Expected: True
    result_b = compare_and_report(4.9, 5.0)   # Expected: False (strict inequality)
    
    print(f"compare_and_report({5.0}, {3.0}) returned: {result_a}")
    print(f"compare_and_report({4.9}, {5.0}) returned: {result_b}")