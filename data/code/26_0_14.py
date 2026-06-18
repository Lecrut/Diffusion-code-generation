def is_greater(a: any, b: any) -> bool:
    """
    Returns True if a is strictly greater than b, False otherwise.
    
    Args:
        a (any): The first value to compare.
        b (any): The second value to compare.
        
    Returns:
        bool: True if a > b, else False.
    """
    return a > b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    print(is_greater(10, 5))      # Expected output: True (integers)
    print(is_greater("z", "a"))   # Expected output: True (strings)
    print(is_greater(3.14, 2.71))# Expected output: True (floats)
    print(is_greater(False, True))# Expected output: False (booleans)