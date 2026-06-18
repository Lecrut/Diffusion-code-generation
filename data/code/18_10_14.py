"""Module to compare two numerical values."""

def is_greater(a: float | int, b: float | int) -> bool:
    """Check if value 'a' is strictly greater than value 'b'.

    Args:
        a (float | int): The first numerical argument.
        b (float | int): The second numerical argument for comparison.

    Returns:
        bool: True if 'a' > 'b', False otherwise.

    Examples:
        >>> is_greater(5, 3)
        True
        >>> is_greater(10, 10)
        False
        
    Notes:
        This function assumes standard ordering for numerical types (int and float).
        It raises a TypeError if non-numerical arguments are provided.
        
    Complexity:
        Time Complexity: O(1) as it performs a single comparison operation.
        Space Complexity: O(1) as no additional memory is allocated during execution.
    
    """
    try:
        return bool(a > b)
    except TypeError:
        # In case non-comparable types are passed, though Python's built-in 
        # comparison will raise this before we even get here usually for numbers.
        # We include explicit handling to be safe if inputs fail type check implicitly.
        raise TypeError("Both arguments must support numeric ordering.")

if __name__ == '__main__':
    sample_a = 10
    sample_b = 5

    result = is_greater(sample_a, sample_b)
    
    print(f"is_greater({sample_a}, {sample_b}) returned: {result}")