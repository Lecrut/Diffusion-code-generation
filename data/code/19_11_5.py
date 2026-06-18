def is_condition_true(a: object, b: object) -> bool:
    """
    Returns True if 'a' is equal to 'b', False otherwise.
    Uses Python's native equality check which is highly optimized in CPython.
    
    Args:
        a: First argument of any type.
        b: Second argument of any type.
        
    Returns:
        A boolean value indicating if a == b.
    """
    return a == b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    samples = [
        (10, 10),       # Should be True
        ("hello", "world"), # Should be False
        ([1, 2], [1, 2]),   # Should be True
        ({'x': 1}, {'x': 1}),# Should be True
        (None, None),    # Should be True
        (True, True),    # Should be True
        ("", ""),         # Should be True
    ]

    for i in range(0, len(samples), 2):
        a = samples[i]
        b = samples[i + 1] if i + 1 < len(samples) else None
        
        result = is_condition_true(a, b)
        
        print(f"is_condition_true({a!r}, {b!r}) -> {result}")