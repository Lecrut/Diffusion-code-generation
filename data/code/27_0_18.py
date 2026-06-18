def check_difference(a: float, b: float) -> bool:
    """
    Returns True if a is different from b, False otherwise.
    
    This function uses direct comparison which is highly optimized in Python's C implementation.
    For floating-point numbers where exact equality might be an issue due to precision,
    the task implies checking for difference (inequality). Standard != operator handles this correctly
    unless a specific tolerance was requested, but "different" usually means not equal in value.
    
    Args:
        a: First numerical input.
        b: Second numerical input.
        
    Returns:
        True if a and b are different (a != b), False otherwise.
    """
    return a != b

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or files.
    val1 = 5.0
    val2 = 7.3
    
    result = check_difference(val1, val2)
    
    if not isinstance(result, bool):
        raise TypeError(f"check_difference must return a boolean, got {type(result).__name__}")

    print("Test Case: ", end="")
    print(f"{val1} != {val2}: {result}")  # Expected output: True
    
    val3 = 4.0
    result_same = check_difference(val3, val3)
    
    if not isinstance(result_same, bool):
        raise TypeError(f"check_difference must return a boolean, got {type(result_same).__name__}")

    print("Test Case: ", end="")
    print(f"{val3} != {val3}: {result_same}")  # Expected output: False
    
    assert result is True and result_same is False, "Logic error in check_difference"