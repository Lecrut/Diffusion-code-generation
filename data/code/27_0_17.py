def check_difference(a: float | int, b: float | int) -> bool:
    """
    Returns True if a is different from b, False otherwise.
    
    This function uses direct comparison which is highly optimized in Python's C implementation.
    It handles both integer and floating-point inputs correctly.

    Args:
        a (int or float): The first numerical value.
        b (int or float): The second numerical value.

    Returns:
        bool: True if the values are different, False otherwise.
    """
    return a != b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    result1 = check_difference(5, 6)
    assert result1 is True

    result2 = check_difference("hello", "world")
    
    print(f"Test 1 (integers): {result1}")