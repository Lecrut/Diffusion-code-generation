def has_repeated_characters(text: str) -> bool:
    text_lower = text.lower()
    seen_chars = set()
    for char in text_lower:
        if char in seen_chars:
            return True
        seen_chars.add(char)
    return False
if __name__ == '__main__':
    sample_strings = [
        "hello",
        "abcdefg",
        "Hello World!",
        "Python Programming"
    ]
    for s in sample_strings:
        result = has_repeated_characters(s)
        print(f"'{s}': {'Has repeated characters' if result else 'No repeated characters'}")