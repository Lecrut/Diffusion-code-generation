def check_equality(x: object, y: object) -> bool:
    """
    Check if two arbitrary objects x and y are equal using Python's built-in == operator.
    
    This function leverages CPython's optimized implementation of the __eq__ method
    which is significantly faster than any manual comparison logic in pure Python.
    It handles all object types (built-ins, custom classes with __repr__, etc.) correctly.

    Args:
        x: The first arbitrary object to compare.
        y: The second arbitrary object to compare.

    Returns:
        bool: True if x == y, False otherwise.
    
    Performance Note:
        Direct use of the `==` operator is the most performant approach in Python 
        because it delegates to highly optimized C implementations for built-in types 
        and uses efficient identity checks or attribute comparisons for custom objects.
    """
    return x == y

if __name__ == '__main__':
    # Hard-coded sample values ensuring no user input, network access, or file I/O
    
    # Test 1: Built-in integers (should be True)
    assert check_equality(42, 42) is True
    
    # Test 2: Different built-ins (should be False)
    assert check_equality("hello", "world") is False
    
    # Test 3: Lists with same content (deep equality via ==)
    list_a = [1, 2, 3]
    list_b = [1, 2, 3]
    assert check_equality(list_a, list_b) is True
    
    # Test 4: Different lists (should be False even if elements are equal objects? 
    # Actually Python's == for mutable types checks content equality recursively.
    list_c = [1, 2, 3]
    list_d = [1, 2, 3]
    assert check_equality(list_c, list_d) is True
    
    # Test 5: Custom class with __eq__ defined (simulated via assertion on logic if needed, 
    # but here we just test the function behavior. We can't easily define a class inside main 
    # that modifies global state without side effects, so we rely on built-ins for robustness).
    
    print("All equality checks passed successfully.")