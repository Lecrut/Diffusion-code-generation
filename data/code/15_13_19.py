def check_equal(a: object, b: object) -> bool:
    """Check if two objects are equal using the built-in equality operator."""
    return a == b

if __name__ == '__main__':
    # Sample test cases with no external dependencies or user input
    assert (1 == 1), "Integers should be equal"
    assert ('hello' == 'hello'), "Strings should be equal"
    assert ([1, 2] == [1, 2]), "Lists should be equal"
    a = {"key": "value"}
    b = {"key": "value"}
    c = {"key": "other"}
    assert (a == b), "Dictionaries with same content should be equal"
    assert not (a == c), "Dictionaries with different content should not be equal"
    
    # Time complexity analysis: O(1) for primitive types, but generally considered constant time in practice 
    # because Python's equality check is implemented as a single C-level operation that compares the object identity or hash and value.
    print("All checks passed.")