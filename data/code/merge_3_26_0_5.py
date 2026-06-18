def is_greater(a: any, b: any) -> bool:
    """
    Returns True if a is strictly greater than b, False otherwise.
    
    Args:
        a: The first value to compare.
        b: The second value to compare.
        
    Returns:
        A boolean indicating whether a > b.
    """
    return a > b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    print(is_greater(10, 5))      # Expected: True
    print(is_greater(3, 7))       # Expected: False
    print(is_greater("z", "a"))   # Expected: True (lexicographical)
    print(is_greater([1,2], [1])) # Expected: True