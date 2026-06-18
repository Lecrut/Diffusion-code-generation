def compare_and_report(num1: float, num2: float) -> bool:
    """
    Checks if two numbers are strictly unequal (num1 != num2).
    
    Parameters:
        num1 (float): The first numeric value to compare.
        num2 (float): The second numeric value to compare.
        
    Returns:
        bool: True if num1 is not equal to num2, otherwise False.
    """
    return num1 != num2

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_cases = [
        (3.5, 7),
        (-4.0, -6.0),
        (0.0, 0.0),
        (1e-9, 2e-9)
    ]

    for n1, n2 in sample_cases:
        result = compare_and_report(n1, n2)
        print(f"compare_and_report({n1}, {n2}) -> {result}")