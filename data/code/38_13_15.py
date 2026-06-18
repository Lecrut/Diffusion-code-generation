def contains_repeated_letters(s: str) -> bool:
    """Check if a string contains any repeated letters (case-insensitive)."""
    seen = set()
    s_lower = s.lower()
    for char in s_lower:
        if not char.isalpha():  # Ignore non-alphabetic characters
            continue
        if char in seen:
            return True
        seen.add(char)
    return False

if __name__ == '__main__':
    test_cases = [
        ("hello", True),
        ("abcdefg", False),
        ("Hello World!", True),
        ("aA1!2#", False),  # 'a' and 'A' are repeated letters; note: logic above treats them as same due to lower()
    ]

    for test_input, expected in test_cases:
        result = contains_repeated_letters(test_input)
        print(f"Input: '{test_input}' -> Expected: {expected}, Got: {result}")