def contains_repeated_letters(s: str) -> bool:
    """Check if a string contains any repeated letters (case-insensitive)."""
    seen = set()
    for char in s.lower():
        if 'a' <= char <= 'z':  # Only consider alphabetic characters
            if char in seen:
                return True
            seen.add(char)
    return False

if __name__ == '__main__':
    test_cases = [
        "hello",      # Expected: True (h, e, llo -> 'l' repeats)
        "abcdef"     # Expected: False (all unique)
    ]

    for text in test_cases:
        result = contains_repeated_letters(text)
        print(f"'{text}': {result}")