def are_equal(item1, item2):
    """
    Returns True if item1 is equal to item2 using Python's equality operator (==),
    False otherwise. Handles integers, strings, lists, and other types correctly.

    Args:
        item1: The first value to compare.
        item2: The second value to compare.

    Returns:
        bool: True if item1 == item2, False otherwise.
    """
    return item1 == item2

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    print(are_equal(5, 5))           # True (integers)
    print(are_equal("hello", "world"))   # False (strings)
    print(are_equal([1, 2], [3, 4]))     # False (lists)
    print(are_equal([1, 2], [1, 2]))     # True (equal lists)
    print(are_equal(True, 1))            # True (True == 1 in Python)