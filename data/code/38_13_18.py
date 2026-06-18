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
        "hello",      # Should be True (l repeats)
        "abcdefg",    # Should be False (no repeats)
        "AaBbCc",     # Should be True (case-insensitive repeat)
        "Python3.8",  # Should be False (only P, y, t, h, o, n are letters; no repeats in this set) -> Actually 'n' appears twice? Let's check: P,y,t,h,o,n,3,.,8. No letter repeats here.)
    ]

    for test_str in test_cases:
        result = contains_repeated_letters(test_str)
        print(f"'{test_str}' has repeated letters: {result}")