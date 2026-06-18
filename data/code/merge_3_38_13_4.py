def contains_repeated_letters(s: str) -> bool:
    """Check if a string contains any repeated letters (case-insensitive)."""
    seen = set()
    s_lower = s.lower()
    for char in s_lower:
        if 'a' <= char <= 'z':  # Only consider alphabetic characters
            if char in seen:
                return True
            seen.add(char)
    return False

if __name__ == '__main__':
    test_cases = [
        ("hello", True),
        ("world", False),
        ("AaBbCc", True),
        ("abcdefg", False),
        ("python", False),
        ("programming", True)
    ]

    for text, expected in test_cases:
        result = contains_repeated_letters(text)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: '{text}' -> {result} (expected {expected})")