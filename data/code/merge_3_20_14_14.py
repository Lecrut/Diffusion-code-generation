def compare_items(a: any, b: any) -> bool:
    """
    Compares two items based on their type equality followed by value equality.
    
    First checks if both arguments have exactly the same type using 'is'.
    If types match, it proceeds to check for standard value equality.
    Returns False immediately if types do not match or if values are unequal.

    Args:
        a (any): The first item to compare.
        b (any): The second item to compare.

    Returns:
        bool: True if both items have the same type and equal value, False otherwise.
    """
    # Preliminary check using 'is' for strict type comparison
    return type(a) is type(b) and a == b

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    # Test case 1: Integers with equal value
    result_int = compare_items(5, 5)
    
    # Test case 2: Strings with different casing (should be False for exact equality unless specified otherwise)
    result_str_case = compare_items("Hello", "hello")
    
    # Test case 3: Lists containing same elements in order
    list_a = [1, 2, 3]
    list_b = [1, 2, 3]
    result_list_eq = compare_items(list_a, list_b)
    
    # Test case 4: Different types (int vs float representing the same number)
    result_type_diff = compare_items(5.0, 5)

    print(f"compare_items(5, 5): {result_int}")      # Expected: True
    print(f"compare_items('Hello', 'hello'): {result_str_case}")   # Expected: False (different strings even if same chars? No, different values) -> Actually "Hello" != "hello", so False. Wait, let's re-evaluate logic. The prompt says standard equality operator. So yes, they are not equal.)
    print(f"compare_items([1, 2], [1, 2]): {result_list_eq}")     # Expected: True (same type and value)
    
    # Test case 5: Same type but different values
    result_val_diff = compare_items(42, 99)   # Expected: False
    
    print(f"compare_items(5.0, 5): {result_type_diff}")     # Expected: False (int is not float via 'is')