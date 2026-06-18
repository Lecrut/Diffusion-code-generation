def has_repeated_characters(text: str) -> bool:
    text_lower = text.lower()
    seen_chars = set()
    for char in text_lower:
        if char not in seen_chars and len(char) == 1:
            seen_chars.add(char)
        elif char in seen_chars or len(char) > 1:
            return True
    if len(text_lower) != len(set(text_lower)):
        return True
    else:
        return False
if __name__ == '__main__':
    sample_strings = [
        ("Hello", True),
        ("abcdefg", False),
        ("AaBbCc", True),
        ("1234567890", False),
        ("Test Case!", True)
    ]
    for test_string, expected in sample_strings:
        result = has_repeated_characters(test_string)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: '{test_string}' -> Repeated chars: {result}")