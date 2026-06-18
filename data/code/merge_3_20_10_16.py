def are_equal(item1: any, item2: any) -> bool:
    """
    Returns True if item1 is equal to item2 using Python's equality operator (==),
    and False otherwise. This works correctly across integers, strings, lists,
    dictionaries, and other comparable types that support __eq__.

    Args:
        item1: The first object to compare.
        item2: The second object to compare.

    Returns:
        True if items are equal, False otherwise.
    """
    return item1 == item2

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    assert are_equal(5, 5) is True      # Integers
    assert are_equal("hello", "hello") is True   # Strings
    assert are_equal([1, 2, 3], [1, 2, 3]) is True     # Lists
    assert are_equal([1, 2], [1, 3]) is False      # Different lists
    assert are_equal(5.0, 5) is True              # Float and int equality
    
    print("All sample tests passed.")