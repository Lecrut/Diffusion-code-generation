def has_repeated_letters(s: str) -> bool:
    """
    Determines if a given string contains any repeated letters (case-insensitive).
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if there are duplicate letters, False otherwise.
    """
    seen = set()
    for char in s.lower():
        # Only consider alphabetic characters; ignore digits and symbols based on "letters" context
        if 'a' <= char <= 'z':
            if char in seen:
                return True
            seen.add(char)
    return False

if __name__ == '__main__':
    test_cases = [
        ("hello", True),
        ("world", False),
        ("A man, a plan...", True),  # 'a' is repeated (case-insensitive)
        ("abcdefg", False),
        ("python", False),
        ("racecar", True),
    ]

    for test_string, expected in test_cases:
        result = has_repeated_letters(test_string)
        print(f"Input: '{test_string}' -> Expected: {expected}, Got: {result}")