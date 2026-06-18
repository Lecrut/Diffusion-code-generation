def contains_repeated_letters(s: str) -> bool:
    """Returns True if any letter appears more than once in the string, ignoring case."""
    seen = set()
    for char in s.lower():
        # Only consider alphabetic characters to ignore digits or symbols
        if 'a' <= char <= 'z':
            if char in seen:
                return True
            seen.add(char)
    return False

if __name__ == '__main__':
    test_cases = [
        ("hello", True),
        ("world", False),
        ("A man a plan, a canal Panama!", True),
        ("1234567890", False),
        ("python programming", True)
    ]

    for text, expected in test_cases:
        result = contains_repeated_letters(text)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: '{text}' -> {result} (expected {expected})")