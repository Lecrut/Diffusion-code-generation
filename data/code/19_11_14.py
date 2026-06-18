def is_condition_true(a: any, b: any) -> bool:
    """
    Returns True if 'a' equals 'b', otherwise False.
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
        (5, 5),          # Should be True
        ("hello", "world"),  # Should be False
        ([1, 2], [3, 4]),   # Should be False
        ({'x': 1}, {'y': 1}), # Should be False
    ]

    for i in range(len(test_cases)):
        a = test_cases[i][0]
        b = test_cases[i][1]
        result = is_condition_true(a, b)
        print(f"Case {i+1}: is_condition_true({a!r}, {b!r}) = {result}")

    # Additional explicit check for identity of same object reference (though == usually suffices)
    obj = [10]
    result_same_obj = is_condition_true(obj, obj)
    print(f"Case Same Object: is_condition_true(obj, obj) = {result_same_obj}")  # Should be True

    final_check = is_condition_true(42, "42")
    print(f"Final Check (int vs str): is_condition_true(42, '42') = {final_check}")  # Should be False