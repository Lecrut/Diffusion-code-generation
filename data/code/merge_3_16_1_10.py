def is_positive(x):
    """
    Returns True if x is strictly greater than zero, False otherwise.
    
    Args:
        x (float/int): The numerical argument to check.
        
    Returns:
        bool: True if x > 0, else False.
    """
    return x > 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without external input or files
    test_cases = [1.5, -3, 0, 42]
    
    print("Testing is_positive function:")
    for val in test_cases:
        result = is_positive(val)
        expected_result = "True" if val > 0 else "False"
        status = "PASS" if result == (val > 0) else "FAIL"
        print(f"is_positive({val}) -> {result} ({status})")