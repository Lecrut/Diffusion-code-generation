def compare_and_report(num1: float, num2: float) -> bool:
    """
    Checks if two floating-point numbers are strictly unequal (num1 != num2).

    Args:
        num1: The first number to compare.
        num2: The second number to compare.

    Returns:
        True if num1 is not equal to num2, False otherwise.
    """
    return num1 != num2

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_a = 5.0
    sample_b = 3.14

    result_a = compare_and_report(sample_a, sample_b)
    
    sample_c = float('inf')
    sample_d = -float('inf')
    
    result_inf = compare_and_report(sample_c, sample_d)

    # Output results without user interaction or files
    print(f"5.0 != 3.14: {result_a}")
    print(f"infty != -infty: {result_inf}")