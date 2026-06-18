def compare_and_report(num1: float, num2: float) -> bool:
    """
    Checks if two floating-point numbers are strictly unequal (not equal).
    
    Args:
        num1 (float): The first numeric value to compare.
        num2 (float): The second numeric value to compare.
        
    Returns:
        bool: True if num1 is not equal to num2, False otherwise.
    """
    return num1 != num2

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    result_1 = compare_and_report(3.0, 5.0)
    print(f"compare_and_report(3.0, 5.0) = {result_1}")

    result_2 = compare_and_report(4.789654, -0.498746)
    print(f"compare_and_report(4.789654, -0.498746) = {result_2}")

    # Test case where values are identical (floating point representation used for precision testing)
    result_3 = compare_and_report(1.0 / 3.0, 1/3 * 1 + 1e-5 - 1e-5)
    print(f"compare_and_report(1.0 / 3.0, 1/3 * 1 + 1e-5 - 1e-5) = {result_3}")