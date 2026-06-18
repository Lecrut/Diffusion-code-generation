def are_equal(item1: object, item2: object) -> bool:
    """
    Compares two items using Python's equality operator (==).
    
    Args:
        item1: The first value to compare.
        item2: The second value to compare.
        
    Returns:
        True if item1 is equal to item2, False otherwise.
    """
    return item1 == item2

if __name__ == '__main__':
    # Test cases with various data types (no user input required)
    
    # Integer comparison
    test_int_1 = are_equal(42, 43)      # Expected: False
    
    # String comparison
    test_str_1 = are_equal("hello", "world")  # Expected: False
    
    # List comparison with same elements in order
    list_a = [10, 20, 30]
    list_b = ["a", "b", "c"]
    
    # Integers (expected True)
    test_int_2 = are_equal(43, 43) 
    print(f"Integer equal: {test_int_2}") 
    
    # Strings with different content (expected False)
    str_a = "hello"
    str_b = "world"
    
    list_c = [10, 20, 30]
    test_list_equal_true_false = are_equal(list_c, list_b) 
    print(f"List vs List (different content): {test_list_equal_true_false}") 
    
    # Test equality with integers
    int_a = 43
    int_b = "43"  
    result_int_string_type_mismatch = are_equal(int_a, int_b)   
    print(f"Integer 'int':{result_int_string_type_mismatch}" if isinstance(result_int_string_type_mismatch,bool) else f"{type(result_int_string_type_mismatch)}")