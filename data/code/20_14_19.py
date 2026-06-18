def compare_items(a: object, b: object) -> bool:
    """
    Compares two items based on their type equality first, 
    then proceeds to value equality if types match.

    Args:
        a (object): The first item to compare.
        b (object): The second item to compare.

    Returns:
        bool: True if both the types are identical and values are equal, False otherwise.
    """
    # Preliminary check using type identity
    if type(a) is not type(b):
        return False
    
    # Proceed with standard equality operator only if types match
    return a == b

if __name__ == '__main__':
    # Sample test cases to demonstrate functionality without external input or files
    samples = [
        (5, 5),                    # Integers: equal type and value -> True
        ("hello", "world"),       # Strings: different types/values -> False
        ([1, 2], [3, 4]),         # Lists: same type but different values -> False
        ({'a': 1}, {'b': 2}),     # Dicts: same type but different keys -> False
        (5.0, 5),                 # Float and Int: different types in Python -> False
        ((3+4j), (7-6j)),         # Complex numbers with equal values -> True
    ]

    print("Running compare_items tests...")
    for i, item_pair in enumerate(samples):
        a, b = item_pair
        result = compare_items(a, b)
        status = "PASS" if result == (a == b) else "FAIL"  # Sanity check against standard operator
        print(f"Test {i+1}: type({type(a).__name__}) vs type({type(b).__name__}): compare_items({repr(a)}, {repr(b)}) -> {result} [{status}]")

    # Explicit demonstration of the 'is' behavior for types that are equal in value but not identity
    print("\nDemonstrating type('int') is int:")
    x = 10
    y = 10
    z = "10"
    
    print(f"type(x) is type(y): {type(x) is type(y)}")      # True (both are <class 'int'>)
    print(f"x == y: {x == y}")                             # True
    
    print(f"type(z) is type(int): {type(z) is int}")       # False (<class 'str'> vs <class 'int'>)