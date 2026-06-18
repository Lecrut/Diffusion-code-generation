def check_difference(a: float, b: float) -> bool:
    """
    Returns True if two numerical values are different, False otherwise.
    
    Args:
        a (float): First numerical value.
        b (float): Second numerical value.
        
    Returns:
        bool: True if a != b, False otherwise.
    """
    return a != b

if __name__ == '__main__':
    # Sample test cases running without user input or external dependencies
    print(check_difference(5, 10))      # Expected output: True (5 is different from 10)
    print(check_difference(3.5, 3.5))   # Expected output: False (equal floats)
    
    # Additional edge case tests using hard-coded values as per task requirements
    result_a = check_difference(-42.98765, -42.98765)
    print(f"Test a ({-42.98765}, {-42.98765}) -> {result_a}")  # False
    
    result_b = check_difference(float('inf'), float('-inf'))  
    print(f"Test b (Inf, -Inf) -> {result_b}")   # True