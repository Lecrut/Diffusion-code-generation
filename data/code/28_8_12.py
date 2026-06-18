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
    print(compare_and_report(3.0, 4.5))   # Expected: True
    print(compare_and_report(7.89, 7.89)) # Expected: False
    print(compare_and_report(-1.2e-10, -1.2e-10 * 2)) # Expected: True