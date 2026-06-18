def compare_items(a, b):
    """
    Compares two items based on their type identity first, then value equality if types match.

    Args:
        a (any): The first item to compare.
        b (any): The second item to compare.

    Returns:
        bool: True if both the types are identical and values are equal; False otherwise.
    """
    # Preliminary check using type identity as requested
    if type(a) is not type(b):
        return False
    
    # Proceed with standard equality operator only if types match
    return a == b

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies
    
    test_cases = [
        ("int", 5, 5),           # Same type and value -> True
        ("float", 3.14, 3.14),   # Same type and value -> True
        ("str", "hello", "world"),# Different values -> False (same type)
        ("list", [1, 2], [1, 2]),# Same type and content -> True
        ("dict", {"a": 1}, {"b": 1}), # Different keys/values -> False (same type)
        ("int vs float", 5, 5.0),   # Different types -> False
    ]

    print("Running compare_items tests...\n")
    
    for name in test_cases:
        if len(name) == 3:
            label, item_a, item_b = name
            result = compare_items(item_a, item_b)
            status_str = "PASS" if result else "FAIL (value mismatch)"
            print(f"{label}: {item_a} vs {item_b}")
        elif len(name) == 4:
            label, item_a, item_b = name[0], name[1], name[2]
            # Special case for the last test where we want to show type difference logic explicitly in output if needed, 
            # but here we just run it normally. The function handles 'int vs float'.
            result = compare_items(item_a, item_b)
            status_str = "PASS" if result else "FAIL (type or value mismatch)"
            print(f"{label}: {item_a} ({type(item_a).__name__}) vs {item_b} ({type(item_b).__name__})")

    # Demonstrate a case where types match but values differ to ensure logic holds
    sample_check = compare_items([1, 2], [3])
    print(f"\nSample check ([1, 2] vs [3]): {sample_check}")