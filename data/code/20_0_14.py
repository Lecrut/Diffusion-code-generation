def are_equal(item1: any = None, item2: any = None) -> bool:
    """
    Returns True if two items are strictly equal using Python's identity 
    or value equality operators where appropriate, ensuring robust handling
    of various data types including lists and tuples.

    Args:
        item1 (any): The first item to compare.
        item2 (any): The second item to compare.

    Returns:
        bool: True if the items are equal, False otherwise.
    
    Note: This function uses Python's standard equality operator (`==`) 
    which handles different data types correctly in most scenarios except for mutable objects 
    where identity is sometimes preferred over value comparison depending on use case requirements,
    but here we prioritize strict semantic equality as per the task description.

    >>> are_equal(5, 5)
    True
    >>> are_equal([1, 2], [1, 2])
    True
    >>> are_equal("hello", "world")
    False
    """
    return item1 == item2

if __name__ == '__main__':
    # Hard-coded sample values for testing without any user input or external dependencies.

    test_cases = [
        (42, 42),              # Integers: strict equality check
        ("hello", "world"),   # Strings should not match
        ([1, 2], [1, 2]),     # Lists with same elements should be equal value-wise in Python
        ((3.5,), (3.5,)),    # Tuples are immutable and compared correctly
        ({'a': 1}, {'b': 1}), # Dictionaries with different keys/values -> False
        ("", ""),             # Empty strings equality check
        ([], []),             # Empty lists should be equal value-wise in Python (unlike Java)
    ]

    for i, pair in enumerate(test_cases):
        item1 = pair[0] if len(pair) > 0 else None
        item2 = pair[1] if len(pair) > 1 else None
        
        # Since the function signature requires two arguments explicitly passed by position or keyword args,
        # we call it directly with these values. For simplicity and robustness:
        
        result = are_equal(item1, item2)

        print(f"Test case {i + 1}: are_equal({item1}, {item2}) -> {result}")