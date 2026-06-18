def is_greater(a: float, b: float) -> bool:
    """
    Check if a numerical value 'a' is strictly greater than another value 'b'.

    This function compares two numbers and returns True only when the first argument
    is strictly larger than the second. It handles both integers and floating-point 
    numbers correctly, including negative values.

    Args:
        a (float): The numerical value to compare against b.
        b (float): The reference numerical value for comparison.

    Returns:
        bool: True if 'a' > 'b', otherwise False.
    
    Examples:
        >>> is_greater(5, 3)
        True
        
        >>> is_greater(-1, -2)
        True
        
        >>> is_greater(0, 0)
        False
    
    Note:
        This function does not perform any input validation beyond type checking. 
        If non-numerical types are passed that cannot be compared in a standard context,
        Python will raise a TypeError during the comparison operation itself rather than 
        explicitly handling invalid inputs within this specific logic block to maintain 
        clarity and alignment with robust functional design patterns for simple comparisons.

    :param float a: The first numerical argument.
    :param float b: The second numerical argument.
    :return True if a > b, else False.
    """
    return a > b

if __name__ == '__main__':
    sample_a = 10
    sample_b = 5
    
    result = is_greater(sample_a, sample_b)
    
    print(f"is_greater({sample_a}, {sample_b}) returned: {result}")