def are_equal(item1: any, item2: any) -> bool:
    """Returns True if item1 equals item2 using Python's equality operator."""
    return item1 == item2

if __name__ == '__main__':
    # Test cases with hard-coded values
    assert are_equal(5, 5) is True      # integers equal
    assert are_equal("hello", "hello") is True   # strings equal
    assert are_equal([1, 2, 3], [1, 2, 3]) is True        # lists equal
    
    print(f"{are_equal(5, 6) = }")         # False
    print(f"{are_equal('a', 'b') = }")   # False