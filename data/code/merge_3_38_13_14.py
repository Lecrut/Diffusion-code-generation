def has_repeated_letters(s: str) -> bool:
    """
    Determines if a given string contains any repeated letters (case-insensitive).
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if there are repeating letters, False otherwise.
    """
    seen = set()
    for char in s.lower():
        if 'a' <= char <= 'z':  # Only consider alphabetic characters a-z
            if char in seen:
                return True
            seen.add(char)
    return False

if __name__ == '__main__':
    test_cases = [
        "hello",      # Should return True (repeated 'l', 'o')
        "abcdef",     # Should return False (all unique)
        "AaBbCc",     # Should return True (case-insensitive match)
        "python",     # Should return False (p, y, t, h, o, n are all unique)
        "",           # Edge case: empty string -> False
    ]

    for test_str in test_cases:
        result = has_repeated_letters(test_str)
        print(f"'{test_str}' contains repeated letters: {result}")