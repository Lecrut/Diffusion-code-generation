def compare_items(a, b):
    """
    Compare two items first by type identity check, then by value equality if types match.

    Args:
        a (any): First item to compare.
        b (any): Second item to compare.

    Returns:
        bool: True if both are of the same type and have equal values, False otherwise.
    """
    # Preliminary check using type identity as requested
    if type(a) is not type(b):
        return False
    
    # Proceed with standard equality operator only if types match
    return a == b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    samples = [
        (5, 5),              # Integers: True
        ("hello", "world"),  # Strings mismatched content: False
        ([1, 2], [3, 4]),   # Lists same type but different values: False
        ({'a': 1}, {'b': 2}), # Dictionaries same type but diff keys/values: False
        (True, True),       # Booleans: True
        ((1+2j), (3+4j)),   # Complex numbers with same real/imag parts would be equal if values matched here but inputs differ: False
    ]

    print("Running compare_items tests...\n")
    
    for i in range(0, len(samples), 2):
        a = samples[i]
        b = samples[i + 1] if (i + 1) < len(samples) else None
        
        # Handle case where second item might be missing intentionally to test type mismatch logic implicitly via function behavior on singletons if needed, 
        # but here we stick to pairs for clarity. If last pair is incomplete in thought process above:
        
        result = compare_items(a, b)
        print(f"compare_items({a}, {b}) = {result}")

    # Additional test case explicitly showing type mismatch returning False immediately
    print("\nAdditional specific check:")
    mixed_type_result = compare_items(10, "ten")
    print(f"compare_items(int 10, string 'ten') = {mixed_type_result}")
    
    same_value_diff_types_check = compare_items([5], [6]) # Same type (list), different value -> False
    print(f"compare_items(lists with diff values) = {same_value_diff_diff_types_check}")