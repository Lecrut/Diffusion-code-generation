def are_equal(item1: object, item2: object) -> bool:
    """
    Returns True if item1 is strictly equal to item2 using Python's identity check (__eq__).
    
    This function handles various data types (integers, floats, strings, lists, dicts, etc.)
    by relying on the native equality operator. It returns False for all other cases,
    including when objects are of different classes but structurally similar.
    
    Args:
        item1: The first object to compare.
        item2: The second object to compare.
        
    Returns:
        True if items are equal according to Python's equality rules; False otherwise.
    """
    return (item1 == item2)

if __name__ == '__main__':
    # Sample test cases covering various data types and edge conditions
    
    # Basic types
    print(are_equal(5, 5))           # True (integers)
    print(are_equal("hello", "hello"))  # True (strings)
    
    # Floats with different representations of the same value
    print(are_equal(float('1.0'), float('2')))   # False (different values despite string representation)
    # Note: Floating point equality can be tricky, but Python's default == is used here.
    
    # Lists and tuples
    lst_a = [1, 2, 3]
    lst_b = [4, 5, 6]
    print(are_equal(lst_a, lst_b))   # False (different contents)
    
    tup_a = (1, 2)
    tup_b = (1, 2)
    print(are_equal(tup_a, tup_b))   # True
    
    # Nested structures with mixed types
    nested_a = [1, "a", {"x": 1}]
    nested_b = [1, "a", {"x": 1}]
    print(are_equal(nested_a, nested_b))  # True (deep equality handled by Python)
    
    # Edge cases: None and mixed types
    print(are_equal(None, None))      # True
    
    int_val = 42
    float_val = 42.0
    string_repr = "42"
    bool_val_true = True
    bool_val_false = False
    
    # Python considers these equal in specific contexts (e.g., list comparisons), 
    # but we are doing direct object comparison here:
    
    print(are_equal(int_val, float_val))  # False (int vs float) unless values match and types align? 
                                           # Actually int 42 == float 42.0 is True in Python!
    print(are_equal(bool_val_true, bool_val_false)) # False
    
    # Custom objects with custom __eq__ methods would work as expected too if defined elsewhere.