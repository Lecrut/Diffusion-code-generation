def has_repeated_characters(s: str) -> bool:
    s_lower = s.lower()
    seen_chars = set()
    for char in s_lower:
        if char in seen_chars:
            return True
        seen_chars.add(char)
    return False
if __name__ == '__main__':
    sample_strings = [
        "hello",
        "abcdefg",
        "The Quick Brown Fox Jumps Over The Lazy Dog"
    ]
    for test_str in sample_strings:
        result = has_repeated_characters(test_str)
        print(f"'{test_str}': {'Repeated characters found' if result else 'No repeated characters'}")