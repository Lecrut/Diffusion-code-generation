def check_equality(x: object, y: object) -> bool:
    """
    Check if two arbitrary objects `x` and `y` are equal using Python's built-in features.
    
    The function prioritizes performance by directly utilizing the identity of the 
    comparison operator (`==`). This is considered optimized as it allows for short-circuiting, 
    efficient type checking at the C level in most cases, and avoids custom logic overhead.

    Args:
        x (object): The first object to compare.
        y (object): The second object to compare.

    Returns:
        bool: True if `x` is equal to `y`, False otherwise.
    
    Note: This function relies on the standard behavior of Python's equality operator, 
    which respects both structural and identity semantics for supported types.
    """
    return x == y

if __name__ == '__main__':
    # Sample test cases running without any user input or external dependencies
    
    # Test 1: Integer comparison (should be True)
    result_int = check_equality(42, 42)
    
    # Test 2: List comparison with different lengths (should be False)
    list_a = [1, 2, 3]
    list_b = [1, 2, 3, 4]
    result_list_diff_len = check_equality(list_a, list_b)
    
    # Test 3: Dictionary comparison with identical keys/values (should be True)
    dict_x = {'a': 1, 'b': 2}
    dict_y = {'a': 1, 'b': 2}
    result_dict_same = check_equality(dict_x, dict_y)
    
    # Test 4: Different types that might look similar but aren't equal (should be False in some contexts 
    # though typically distinct objects are not considered equal unless explicitly designed so).
    # Here we use a simple case where one is an int and another is a string.
    result_mixed = check_equality(5, "5")

    print(f"Integer Equality: {result_int}")           # Expected: True
    print(f"Different List Lengths: {result_list_diff_len}")  # Expected: False
    print(f"Ideal Dictionary Equality: {result_dict_same}")      # Expected: True
    print(f"Mixed Types (int vs str): {result_mixed}")          # Expected: False