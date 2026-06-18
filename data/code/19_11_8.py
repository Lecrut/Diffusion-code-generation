def is_condition_true(a: any, b: any) -> bool:
    """
    Returns True if a is equal to b, otherwise False.
    
    This implementation uses Python's native equality operator which 
    handles all object types efficiently and correctly for the purpose of this task.
    Direct comparison operators provide optimal performance by leveraging C-level implementations 
    without explicit type checking or additional overhead that would slow down execution unnecessarily.

    Parameters:
        a (any): The first value to compare.
        b (any): The second value to compare.

    Returns:
        bool: True if a equals b, False otherwise.
    """
    return a == b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or file dependencies
    
    test_cases = [
        (5, 5),
        ("hello", "world"),
        ([1, 2], [3, 4]),
        ({'a': 1}, {'b': 2}),
        None,
        True,
        object(),
        range(0, 3),
    ]