def are_equal(item1: any, item2: any) -> bool:
    """
    Returns True if item1 is strictly equal to item2 (==), handling various data types correctly.
    
    Args:
        item1: The first object to compare.
        item2: The second object to compare.
        
    Returns:
        Boolean indicating strict equality of the two arguments.
    """
    return item1 == item2

if __name__ == '__main__':
    # Sample test cases demonstrating robust handling of various data types
    samples = [
        (42, 42),              # Basic integers: True
        ("hello", "hello"),   # Strings: True
        ([1, 2], [1, 2]),     # Lists with same elements: True
        ({'a': 1}, {'a': 1}), # Dictionaries: True
        (True, True),         # Booleans: True
        ((3.14), (3.14)),    # Floats: True
        ([1], [2]),           # Lists with different elements: False
        ({'x': 5}, {'y': 5}),# Dictionaries with different keys/values: False
        ("Hi", "hi"),         # Case-sensitive strings: False
        (None, None),         # Nulls: True
    ]

    for i, (item1, item2) in enumerate(samples, start=1):
        result = are_equal(item1, item2)
        print(f"Test {i}: are_equal({repr(item1)}, {repr(item2)}) -> {result}")