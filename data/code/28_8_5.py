def compare_and_report(num1: float, num2: float) -> bool:
    """
    Returns True if num1 is strictly greater than num2, otherwise False.
    
    Parameters:
        num1 (float): The first numeric value to compare.
        num2 (float): The second numeric value to compare against num1.
        
    Returns:
        bool: True if num1 > num2, else False.
    """
    return num1 > num2

if __name__ == '__main__':
    # Sample values for testing without user input or external dependencies
    sample_values = [
        (5.0, 3.0),      # Expected: True
        (3.0, 5.0),      # Expected: False
        (-1.0, -2.0),    # Expected: True (negative comparison)
        (42.7, 42.69),   # Expected: True
        (float('inf'), float('-inf')),  # Expected: True
    ]

    for val in sample_values:
        a, b = val[0], val[1]
        result = compare_and_report(a, b)
        print(f"compare_and_report({a}, {b}) -> {result}")