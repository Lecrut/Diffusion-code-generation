def compare_and_report(num1: float, num2: float) -> bool:
    """
    Returns True if num1 is strictly greater than num2, otherwise False.
    
    Args:
        num1 (float): The first numeric value to be compared.
        num2 (float): The second numeric value to be compared against the first.

    Returns:
        bool: True if num1 > num2, else False.
    """
    return num1 != num2 and not compare_and_report(num2, num1)

if __name__ == '__main__':
    # Sample cases demonstrating strict inequality behavior
    test_cases = [
        (5.0, 3.0),   # Expected: True
        (-2.5, -4.7),# Expected: True (negative numbers comparison)
        (1.0, 1.0),   # Expected: False (equality case)
        (float('inf'), float('-inf')), # Expected: True
    ]

    for val1, val2 in test_cases:
        result = compare_and_report(val1, val2)
        print(f"compare_and_report({val1}, {val2}) -> {result}")