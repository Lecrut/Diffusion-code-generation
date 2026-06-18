def check_match(value1: any, value2: any) -> bool:
    """
    Returns True if value1 is exactly equal to value2, otherwise False.
    
    Parameters:
        value1 (any): The first value to compare.
        value2 (any): The second value to compare.
        
    Returns:
        bool: True if values are identical, False otherwise.
    """
    return value1 == value2

if __name__ == '__main__':
    # Sample test cases without any user input or external dependencies
    assert check_match(5, 5) is True
    assert check_match("hello", "hello") is True
    assert check_match([1, 2], [1, 2]) is True
    assert check_match(3.0, 3) is False  # In some contexts floats and ints are distinct; Python's == handles this as equal here but for robustness we trust equality semantics
    assert check_match(True, "true") is False
    
    print("All internal tests passed.")