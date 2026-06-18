def compare_items(a: object, b: object) -> bool:
    """
    Compares two items by first checking if they share the same type.
    If types match, it proceeds to check for value equality using '=='.
    
    Args:
        a (object): The first item to compare.
        b (object): The second item to compare.
        
    Returns:
        bool: True if both items are of the same type and equal in value; False otherwise.
    """
    return type(a) is type(b) and a == b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    
    # Test 1: Integers (should be True)
    result_1 = compare_items(5, 5)
    
    # Test 2: Strings (should be False due to different content)
    result_2 = compare_items("hello", "world")
    
    # Test 3: Different types with same value representation (e.g., int vs float '5' and 5.0, but type check fails)
    # Note: '5' is str, 5 is int -> False due to type mismatch
    
    # Test 4: Lists of different lengths (should be False)
    result_4 = compare_items([1, 2], [1])
    
    # Test 5: None values (should be True)
    result_5 = compare_items(None, None)
    
    # Print results to verify functionality without user input
    print(f"Test 1 (Integers): {result_1}")      # Expected: True
    print(f"Test 2 (Strings): {result_2}")   # Expected: False
    print(f"Test 3 (Different types '5' vs 5): {compare_items('5', 5)}")             # Expected: False
    print(f"Test 4 (Lists different length): {result_4}")                           # Expected: False
    print(f"Test 5 (None values): {result_5}")                                      # Expected: True
    
    # Additional edge case test for mixed types that look equal but aren't the same type
    result_mixed = compare_items([1, 2], [3])
    
    if __name__ == '__main__':
        print(f"Test Mixed Lists: {result_mixed}")   # Expected: False (different contents)