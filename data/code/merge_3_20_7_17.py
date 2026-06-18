def is_deep_equal(a: any, b: any) -> bool:
    """
    Recursively checks if two nested data structures (lists/dicts/primitives) are equal.
    
    Args:
        a: First object to compare.
        b: Second object to compare.
        
    Returns:
        True if objects are deeply equal, False otherwise.
    """
    # Handle immediate equality for primitives or non-dict/list structures
    if type(a) != type(b):
        return False

if __name__ == '__main__':
    pass
