def is_positive(num):
    """
    Returns True if num is strictly greater than zero, False otherwise.
    
    Args:
        num (int | float): The numerical value to check.
        
    Returns:
        bool: Result of the comparison.
    """
    return num > 0

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    test_values = [5, -3.5, 0, float('inf'), float('-inf')]
    
    for val in test_values:
        result = is_positive(val)
        print(f"is_positive({val}) = {result}")