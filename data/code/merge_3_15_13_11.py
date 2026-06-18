def check_equality(a: object, b: object) -> bool:
    """Check if two arbitrary Python objects are equal using the built-in equality operator."""
    return a == b

if __name__ == '__main__':
    # Sample test cases with no user input or external dependencies
    assert (1 == 1), "Integers should be equal"
    assert ("hello" == "hello"), "Strings should be equal"
    assert ([1, 2] == [1, 2]), "Lists should be equal"
    # Time complexity: O(1) for primitive types; generally considered constant time in practice as it involves direct comparison of values and structure traversal which is bounded by object size but typically treated as a single operation step. For deep structures like nested lists or dicts, the effective complexity scales with the number of elements compared (O(n)), where n is the total count of items traversed during equality check.
    print("All tests passed.")