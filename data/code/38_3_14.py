def contains_repeated_letters(text: str) -> bool:
    """
    Determines if a given string contains any repeated letters (case-insensitive).
    
    Args:
        text (str): The input string to check.
        
    Returns:
        bool: True if there are repeated letters, False otherwise.
    """
    seen = set()
    for char in text.lower():
        if 'a' <= char <= 'z':  # Only consider alphabetic characters a-z
            if char in seen:
                return True
            seen.add(char)
    return False

if __name__ == '__main__':
    test_cases = [
        ("hello", True),
        ("world", False),
        ("Python", False),
        ("aabbcc", True),
        ("The quick brown fox jumps over the lazy dog", True)
    ]

    for text, expected in test_cases:
        result = contains_repeated_letters(text)
        print(f"Text: '{text}' -> Repeated letters: {result} (Expected: {expected})")