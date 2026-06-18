def check_equality(x: object, y: object) -> bool:
    """
    Check if two arbitrary objects x and y are equal using Python's built-in == operator.
    
    This function leverages Python's optimized C-level implementation of the __eq__ method,
    which is generally faster than manual comparison logic for most data types (integers, floats, strings, lists, dicts).

    Args:
        x: The first object to compare.
        y: The second object to compare.

    Returns:
        bool: True if x == y, False otherwise.
    
    Note: This function does not perform deep structural comparison for all cases (e.g., it relies on the 
    __eq__ implementation of the specific types). For objects without a defined __eq__, Python falls back to identity check (__id__).
    """
    return x == y

if __name__ == '__main__':
    # Hard-coded sample values for testing
    test_cases = [
        (5, 5),           # Integers: True
        ("hello", "world"),   # Strings: False
        ([1, 2], [3, 4]),     # Lists: False
        ({'a': 1}, {'b': 2}),    # Dicts: False
        (True, True),       # Booleans: True
        ((1+1j), (1+1j)),   # Complex numbers: True
        ([], []),           # Empty lists: True
        ("", ""),           # Empty strings: True
        (None, None),       # Nulls: True
    ]

    for i, (x_val, y_val) in enumerate(test_cases):
        result = check_equality(x_val, y_val)
        print(f"Test case {i+1}: x={repr(x_val)}, y={repr(y_val)} -> Equal? {result}")