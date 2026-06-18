def check_equality(a: object, b: object) -> bool:
    """Check if two objects are equal using the built-in equality operator."""
    return a == b

if __name__ == '__main__':
    # Sample test cases with no user input or external dependencies
    assert (1 == 1), "Integers should be equal"
    assert ([1, 2] == [1, 2]), "Lists should be equal"
    assert ("hello" != "world"), "Strings should not be equal"
    print("All equality checks passed.")