def compare_and_report(num1: float, num2: float) -> bool:
    """
    Check if two floating-point numbers are strictly unequal.
    
    Args:
        num1 (float): The first number to compare.
        num2 (float): The second number to compare.
        
    Returns:
        bool: True if num1 is not equal to num2, False otherwise.
    """
    return num1 != num2

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    result_1 = compare_and_report(5.0, 3.14)
    result_2 = compare_and_report(7.89, -7.89)
    result_3 = compare_and_report(10.0, 10.0)

    print(f"compare_and_report(5.0, 3.14): {result_1}")
    print(f"compare_and_report(7.89, -7.89): {result_2}")
    print(f"compare_and_report(10.0, 10.0): {result_3}")