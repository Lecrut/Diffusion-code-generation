def compare_and_report(num1: float, num2: float) -> bool:
    """
    Checks if two floating-point numbers are strictly unequal.

    Args:
        num1 (float): The first number to compare.
        num2 (float): The second number to compare.

    Returns:
        bool: True if num1 is not equal to num2, False otherwise.
    """
    return num1 != num2

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_cases = [
        (3.5, 4.0),      # Should be True
        (7.0, 7.0),      # Should be False
        (-1.23, -1.23), # Should be False
        (float('inf'), float('-inf')), # Should be True
    ]

    for a, b in sample_cases:
        result = compare_and_report(a, b)
        print(f"compare_and_report({a}, {b}) = {result}")