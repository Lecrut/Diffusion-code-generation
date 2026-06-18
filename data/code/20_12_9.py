def are_equal(x: object, y: object) -> bool:
    """
    Check if two arbitrary objects `x` and `y` are equal using Python's built-in features.
    
    The function prioritizes performance by directly invoking the `==` operator.
    This leverages C-level optimizations for most data types in the standard library,
    avoiding overhead from explicit type checks or custom logic unless necessary.
    
    Args:
        x (object): The first object to compare.
        y (object): The second object to compare.
        
    Returns:
        bool: True if `x` is equal to `y`, False otherwise.
    """
    return x == y

if __name__ == '__main__':
    # Sample tests with hard-coded values, no user input or external dependencies
    
    test_cases = [
        (5, 5),                    # Integers are equal
        ([1, 2], [1, 2]),         # Lists with same content are equal
        ('hello', 'hello'),       # Strings match exactly
        (3.14, 3.14),             # Floats compare based on value representation
        ((True,), (False,)),      # Tuples of different booleans not equal
        
        ([], []),                  # Empty lists are equal
        ({}, {}),                  # Dictionaries with same keys/values might be deep compared but here shallow if just empty? 
                                   # Actually dict comparison is full: {1:'a'} == {1:'a'}. Let's test non-empty.
    ]

    sample_objects = [
        (42, 43),               # Unequal ints
        ([0], []),              # List with element vs empty list
        ('world', 'Earth'),     # Different strings
        
        ("abc", "ABC"),         # Case-sensitive string comparison expected to be False
    ]

    results = {}
    
    for i, (a, b) in enumerate(test_cases + sample_objects):
        is_equal = are_equal(a, b)
        print(f"Test {i}: Input={repr(a)}, Input2={repr(b)} | Equal: {is_equal}")