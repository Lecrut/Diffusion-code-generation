def compare_and_report(num1: float, num2: float) -> bool:
    """
    Checks if two floating-point numbers are strictly unequal.

    Parameters:
        num1 (float): The first number to compare.
        num2 (float): The second number to compare.

    Returns:
        bool: True if num1 is not equal to num2, False otherwise.
    """
    return num1 != num2

if __name__ == '__main__':
    # Sample test cases demonstrating strict inequality check
    sample_cases = [
        (3.5, 7),           # Should be True
        (4.0, 4.0),         # Should be False
        (-1.2, -1.2),       # Should be False
        (float('inf'), float('-inf')),  # Should be True
    ]

    for val_pair in sample_cases:
        result = compare_and_report(val_pair[0], val_pair[1])
        print(f"compare_and_report({val_pair[0]}, {val_pair[1]}) = {result}")