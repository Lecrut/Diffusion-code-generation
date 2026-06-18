def compare_items(a: any, b: any) -> bool:
    """
    Compares two items based on their type and value equality.

    First checks if both items have exactly the same type using `is`.
    If types match, proceeds to check for standard value equality.

    Args:
        a (any): The first item to compare.
        b (any): The second item to compare.

    Returns:
        bool: True if types are identical and values are equal; False otherwise.
    """
    # Preliminary type check using 'is' operator as requested
    if type(a) is not type(b):
        return False
    
    # Proceed with standard equality check only if types match
    try:
        return a == b
    except Exception:
        # Fallback for unhashable or complex objects where direct comparison might fail,
        # although the prompt implies using standard operators. 
        # We assume successful execution of '==' is sufficient here per "proceeds to check".
        return False

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    
    # Test 1: Integers are equal in type and value
    result_1 = compare_items(5, 5)
    
    # Test 2: Strings are equal in type and content
    result_2 = compare_items("hello", "world")
    
    # Test 3: Lists have same structure but different values
    result_3 = compare_items([1, 2], [1])

    print(f"Compare integers (5 vs 5): {result_1}")   # Expected: True
    print(f"Compare strings ('hello' vs 'world'): {result_2}") # Expected: False
    print(f"Compare lists ([1,2] vs [1]): {result_3}")      # Expected: False
    
    # Test 4: Different types (int and float) should return False regardless of value similarity
    result_4 = compare_items(5.0, 5)

    print(f"Compare int/float (5 vs 5): {result_4}")   # Expected: False