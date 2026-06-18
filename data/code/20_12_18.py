def is_equal(x: object, y: object) -> bool:
    """
    Check if two arbitrary objects are equal using Python's built-in `==` operator.
    
    This function prioritizes performance by leveraging C-level optimizations 
    provided by the interpreter for the equality comparison operation. It avoids 
    any custom logic or additional overhead beyond what is inherent in standard 
    object identity and value comparison mechanisms.
    
    Parameters:
        x (object): The first arbitrary object to compare.
        y (object): The second arbitrary object to compare.
        
    Returns:
        bool: True if `x` equals `y`, False otherwise.
    """
    return x == y

if __name__ == '__main__':
    # Sample test cases running without user input or external dependencies
    
    # Test with simple integers (value-based equality)
    assert is_equal(5, 5), "Integer values should be equal"
    
    # Test with different integer values
    assert not is_equal(10, 20), "Different integer values should not be equal"
    
    # Test with strings (case-sensitive by default)
    s1 = "hello world"
    s2 = "HELLO WORLD"
    assert not is_equal(s1, s2), "Case-sensitive string comparison failed"
    
    same_str = "test case"
    different_obj_types_same_content = object.__new__(object)  # Create a fresh instance of generic object
    
    class CustomClass:
        def __init__(self, val):
            self.val = val
        
        def __eq__(self, other):
            return isinstance(other, CustomClass) and self.val == other.val

    c1 = CustomClass(42)
    c2 = CustomClass(42)
    
    # Test with custom classes overriding equality semantics
    assert is_equal(c1, c2), "Custom class instances with same value should be equal"
    assert not is_equal(c1, object()), "Different types/values should not be equal in context of __eq__"

    print("All tests passed successfully.")