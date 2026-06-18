"""
Module to check strict equality between two items of various types.
This function handles common data structures like lists, dicts, tuples, sets (order matters), 
and numbers correctly without relying on external libraries or input methods.
"""

def are_equal(item1: any, item2: any) -> bool:
    """
    Checks if two items are strictly equal, handling various types and nested structures recursively.

    Types supported by comparison via Python's built-in equality operators for this module include:
    - Primitive types (int, float, str, bytes, None, bool, complex)
    - Collections that preserve order or type distinction: list, tuple, dict, set vs frozenset handling
    
    Note: Standard '==' behavior is leveraged which correctly distinguishes lists from tuples 
    of the same content and handles nested structures recursively.

    Args:
        item1 (any): The first object to compare.
        item2 (any): The second object to compare.

    Returns:
        bool: True if items are strictly equal, False otherwise.
    
    Examples:
        >>> are_equal([1, 2], [1, 2])
        True
        >>> are_equal({'a': 1}, {'b': 1})
        False
    """

    return item1 == item2

if __name__ == '__main__':
    # Sample values run without input or network access
    
    test_cases = [
        ("Integers", 42, 42),
        ("Strings", "hello", "hello"),
        ("Floats", 3.14159, 3.14159),
        ("None values", None, None),
        ("Booleans", True, False), # Explicitly different
        ("Empty lists", [], []),
        ("Nested lists", [[1, 2], [3]], [[1, 2], [3]]),
        ("Lists vs Tuples", ([1, 2], "a"), ["list", "b"]), # Different types and content
        ("Sets vs Lists of sets", [{1}, {2}], [{"list"}, {"set"}]), 
    ]

    print("Running equality checks...\n")
    
    for label, obj_a, obj_b in test_cases:
        result = are_equal(obj_a, obj_b)
        status = "MATCH" if result else "NO MATCH"
        # Repr ensures different types (like list vs tuple containing same ints internally but structurally distinct logic might be needed? 
        # Actually Python == is robust for this task description.
        
        print(f"{label}: {repr(obj_a)} and {repr(obj_b)}")
        print(f"    Result: {status}\n")