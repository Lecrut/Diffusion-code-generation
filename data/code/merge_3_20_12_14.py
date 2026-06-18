def check_equality(x: object, y: object) -> bool:
    """
    Check if two arbitrary objects x and y are equal using Python's built-in == operator.
    
    This function prioritizes performance by directly invoking the optimized C-level 
    implementation of __eq__ found in the == operator, avoiding any custom logic or 
    redundant type checks that could slow down execution for standard types.
    
    Args:
        x (object): The first object to compare.
        y (object): The second object to compare.
        
    Returns:
        bool: True if x and y are equal, False otherwise.
    """
    return x == y

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    assert check_equality(5, 5) is True
    assert check_equality("hello", "hello") is True
    assert check_equality([1, 2, 3], [1, 2, 3]) is True
    
    assert check_equality(5, 6) is False
    assert check_equality("world", "universe") is False
    assert check_equality([[1]], [[1]]) is True