def check_equality(x: object, y: object) -> bool:
    """
    Optimized function to check if two arbitrary objects are equal.
    Uses Python's built-in == operator which is implemented in C and highly efficient.
    
    Args:
        x (object): The first object to compare.
        y (object): The second object to compare.
        
    Returns:
        bool: True if x equals y, False otherwise.
    """
    return x == y

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    # Test case 1: Integers and floats (exact match)
    assert check_equality(42, 42) is True
    assert check_equality(3.14, 3.14) is False

    # Test case 2: Different types that might look similar but aren't equal
    assert check_equality("hello", "HELLO") is False
    
    # Test case 3: Lists and tuples (content comparison via == operator)
    assert check_equality([1, 2, 3], [1, 2, 3]) is True
    assert check_equality((1, 2), [1, 2]) is False

    # Test case 4: Objects with custom __eq__ implementation simulation (using built-in objects)
    class CustomObj:
        def __init__(self, value):
            self.value = value
        
        def __repr__(self):
            return f"CustomObj({self.value})"

    obj1 = CustomObj(10)
    obj2 = CustomObj(10)
    
    # Note: By default, objects use identity for equality unless __eq__ is defined.
    # This demonstrates that == works on built-in features and custom classes.
    assert check_equality(obj1, obj2) is False

    print("All tests passed successfully.")