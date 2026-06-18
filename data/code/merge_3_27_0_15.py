def check_difference(a: float, b: float) -> bool:
    """
    Returns True if a is different from b, False otherwise.
    
    This function uses direct comparison which is highly optimized in Python's C implementation.
    It handles all numerical types (int and float). For floating point numbers, it checks for inequality directly,
    avoiding unnecessary epsilon comparisons unless specific tolerance logic was requested (which is not per task requirements).

    Args:
        a: First numerical value.
        b: Second numerical value.

    Returns:
        bool: True if a != b, False otherwise.
    """
    return a != b

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies
    val1 = 5
    val2 = 3
    
    result = check_difference(val1, val2)
    
    if not isinstance(result, bool):
        raise TypeError("Function must return a boolean value.")

    print(f"Are {val1} and {val2} different? {result}")