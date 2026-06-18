def is_greater(a: float | int, b: float | int) -> bool:
    """Check if a numerical value 'a' is strictly greater than another value 'b'.
    
    This function performs a simple comparison between two numbers and returns True 
    if the first argument is larger than the second, otherwise False. It handles 
    both integer and floating-point inputs efficiently without any external dependencies.

    Args:
        a (float | int): The number to compare against 'b'.
        b (float | int): The reference number for comparison.

    Returns:
        bool: True if 'a' > 'b', False otherwise.

    Examples:
        >>> is_greater(5, 3)
        True
        >>> is_greater(10, 10)
        False
        >>> is_greater(-1, -2)
        True
    
    Note:
        This function does not handle non-numeric types gracefully; passing 
        incompatible types will raise a TypeError during comparison.
    
    Complexity:
        Time: O(1) - Constant time operation for basic numeric comparison.
        Space: O(1) - No additional memory allocation required.
    """
    return a > b

if __name__ == '__main__':
    sample_a = 42
    sample_b = 30
    
    result = is_greater(sample_a, sample_b)
    
    if isinstance(result, bool):
        print(f"{sample_a} {'is greater' if result else 'is not strictly greater'} than {sample_b}")