def has_repeated_letters(text: str) -> bool:
    """
    Determines if a given string contains any repeated letters (case-insensitive).
    
    Args:
        text (str): The input string to check.
        
    Returns:
        bool: True if there are repeated letters, False otherwise.
    """
    seen = set()
    for char in text.lower():
        # Only consider alphabetic characters and ignore others like digits or spaces
        if 'a' <= char <= 'z':
            if char in seen:
                return True
            seen.add(char)
    return False

if __name__ == '__main__':
    test_cases = [
        ("hello", True),       # h, e, l, o -> l repeats
        ("abcdef", False),     # all unique
        ("Hello World!", True),# H and h count as repeat if we consider case-insensitive (but here only 'l' is repeated)
        ("a1b2c3", False),    # no letters repeat
        ("aaa", True),         # a repeats multiple times
        ("The quick brown fox jumps over the lazy dog", True),       # t, h, e appear multiple times (case-insensitive logic applies to 't' in The and the)
    ]

    for test_input, expected_result in test_cases:
        result = has_repeated_letters(test_input)
        status = "PASS" if result == expected_result else "FAIL"
        print(f"[{status}] Input: '{test_input}' -> Expected: {expected_result}, Got: {result}")