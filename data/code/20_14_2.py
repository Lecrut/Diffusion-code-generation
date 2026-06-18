def compare_items(a: object, b: object) -> bool:
    """
    Compares two items first by checking if their types match exactly using `is`,
    and then checks for value equality using the standard equality operator if they do.

    Args:
        a (object): The first item to compare.
        b (object): The second item to compare.

    Returns:
        bool: True if both items have the same type and are equal, False otherwise.
    """
    return type(a) is type(b) and a == b

if __name__ == '__main__':
    # Sample test cases demonstrating various scenarios
    
    # Test 1: Integers with different values (types match, value differs)
    result_int_diff = compare_items(5, 10)
    
    # Test 2: Strings that are equal (types and values match)
    result_str_eq = compare_items("hello", "hello")
    
    # Test 3: Lists with same content but different order or length (value differs)
    list_a = [1, 2, 3]
    list_b = [1, 3, 2]
    result_list_diff_order = compare_items(list_a, list_b)
    
    # Test 4: Different types that happen to have equal values (e.g., int vs float representation of same number)
    result_type_mismatch = compare_items(5.0, 5)
    
    # Print results for verification
    print(f"compare_items(5, 10): {result_int_diff}")      # Expected: False (values differ)
    print(f"compare_items('hello', 'hello'): {result_str_eq}")   # Expected: True
    print(f"compare_items([{1}, {2}, {3}], [{1}, {3}, {2}]): {result_list_diff_order}")  # Expected: False
    print(f"compare_items(5.0, 5): {result_type_mismatch}")     # Expected: False (types differ)