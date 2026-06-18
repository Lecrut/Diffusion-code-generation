def check_difference(value1: float | int, value2: float | int) -> bool:
    """
    Returns True if value1 is different from value2, False otherwise.
    
    This function uses Python's built-in != operator which is highly optimized in CPython
    and handles all numeric types (int and float). For floating-point numbers, it relies on
    standard IEEE 754 comparison semantics rather than implementing a custom epsilon check
    unless specific tolerance requirements were provided.

    Args:
        value1: First numerical input (int or float)
        value2: Second numerical input (int or float)

    Returns:
        bool: True if the inputs are different, False otherwise
    """
    return value1 != value2

if __name__ == '__main__':
    pass
