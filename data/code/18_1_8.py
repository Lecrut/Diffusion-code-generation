import sys

def is_greater(a: float | int, b: float | int) -> bool:
    """
    Returns True if a > b, otherwise False.
    
    Args:
        a (float|int): First numerical argument.
        b (float|int): Second numerical argument.
        
    Returns:
        bool: Result of comparison a > b.
    """
    return a > b

if __name__ == '__main__':
    # Sample values for testing without external input or files
    sample_a = 10
    sample_b = 5
    
    result = is_greater(sample_a, sample_b)
    
    print(result)