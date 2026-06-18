def are_equal(item1: any, item2: any) -> bool:
    """
    Returns True if item1 is equal to item2 using Python's equality operator (==),
    and False otherwise. Works correctly with integers, strings, lists, and other types.
    
    Args:
        item1: The first item to compare.
        item2: The second item to compare.
        
    Returns:
        A boolean indicating whether the two items are equal.
    """
    return item1 == item2

if __name__ == '__main__':
    # Sample test cases with various data types
    assert are_equal(5, 5) is True       # Integers
    assert are_equal("hello", "hello") is True   # Strings
    
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    
    assert are_equal(list_a, list_a) is True     # Same reference
    assert are_equal([1, 2], [1, 2]) is True      # Equal content
    
    print(f"Tested {are_equal(5, 5)} (int)")
    print(f"Tested {are_equal('hello', 'hello')} (str)")
    print(f"Tested {are_equal([1, 2], [1, 2])} (list)")