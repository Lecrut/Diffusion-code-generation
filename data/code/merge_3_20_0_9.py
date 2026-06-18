def are_equal(item1: any, item2: any) -> bool:
    """
    Returns True if item1 is strictly equal to item2, handling various data types correctly.
    
    Args:
        item1 (any): The first value to compare.
        item2 (any): The second value to compare.
        
    Returns:
        bool: True if the values are exactly equal, False otherwise.
    """
    return item1 == item2

if __name__ == '__main__':
    # Sample test cases with no user input or external dependencies
    
    # Test integers and floats (note: float equality can be tricky but we use standard '==')
    assert are_equal(42, 42) is True
    assert are_equal(3.14, 3.14) is True
    assert are_equal("hello", "world") is False
    
    # Test different types (int vs float with same representation - usually considered not equal in strict type sense unless values match numerically, but here we use value equality via '==')
    assert are_equal(5, 5.0) is True  # In Python, int and float can be compared by value
    
    # Test lists (deep comparison for elements at same indices)
    list1 = [1, "a", None]
    list2 = [1, "a", None]
    assert are_equal(list1, list2) is True
    
    list3 = [1, 2, 3]
    list4 = [1, 2, 3, 4]
    assert are_equal(list3, list4) is False
    
    # Test dictionaries (deep comparison for keys and values)
    dict1 = {"x": 10, "y": 20}
    dict2 = {"x": 10, "y": 20}
    assert are_equal(dict1, dict2) is True
    
    d3 = {1: "one"}
    d4 = {(1): ("one")} # Note: tuple keys vs int key comparison might differ in type but here we just check equality of the objects themselves passed as args. 
                      # Let's stick to simple structural equality for dicts with same content types
    
    assert are_equal({"a": 1}, {"b": 2}) is False
    assert are_equal({}, {}) is True
    
    # Test mixed types that shouldn't be equal even if values look similar (e.g., list vs tuple)
    assert are_equal([1, 2], (1, 2)) is False
    
    print("All sample tests passed.")