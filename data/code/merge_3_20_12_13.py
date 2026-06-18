def check_equality(x: object, y: object) -> bool:
    """
    Check if two arbitrary objects x and y are equal using Python's built-in == operator.
    
    This function leverages Python's optimized C-level implementation of the equality 
    comparison to ensure maximum performance for both primitive types (integers, floats, strings)
    and complex custom classes that have implemented __eq__.

    Args:
        x: The first object to compare.
        y: The second object to compare.

    Returns:
        bool: True if x is equal to y according to the == operator, False otherwise.
    
    Examples:
        >>> check_equality(10, 10)
        True
        >>> check_equality([1, 2], [1, 2])
        True
        >>> check_equality("hello", "world")
        False
    """
    return x == y

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    # Test with integers (primitive types)
    assert check_equality(42, 42), "Integer equality failed"
    
    # Test with floats
    pi_val = 3.141592653589793
    assert check_equality(pi_val, pi_val), "Float equality failed"
    
    # Test with strings
    word = "Python"
    assert not check_equality(word, "Java"), "String inequality test failed"
    
    # Test with lists (mutable sequences)
    sample_list = [10, 20, 30]
    assert check_equality(sample_list, [40, 50]), "List equality failed - should be False"
    other_list = [10, 20, 30]
    assert check_equality(sample_list, other_list), "Identical list equality failed"
    
    # Test with tuples (immutable sequences)
    tuple_a = ("a", "b")
    tuple_b = ("c", "d")
    assert not check_equality(tuple_a, tuple_b), "Tuple inequality test failed"
    
    print("All internal tests passed successfully.")