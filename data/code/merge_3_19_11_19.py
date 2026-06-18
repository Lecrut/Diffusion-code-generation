def is_condition_true(a: any, b: any) -> bool:
    """
    Returns True if 'a' is equal to 'b', otherwise False.
    Uses Python's built-in equality operator which handles various types efficiently.
    
    Args:
        a: First value to compare.
        b: Second value to compare.
        
    Returns:
        bool: True if a == b, else False.
    """
    return a == b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        (5, 5),           # Should be True
        ("hello", "world"),   # Should be False
        ([1, 2], [3, 4]),     # Should be False
        ({'x': 1}, {'x': 1}), # Should be True
        (None, None),      # Should be True
    ]

    for i, case in enumerate(test_cases):
        a_val = case[0]
        b_val = case[1]
        result = is_condition_true(a_val, b_val)
        print(f"Test {i+1}: is_condition_true({a_val!r}, {b_val!r}) => {result}")