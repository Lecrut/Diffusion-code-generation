def has_repeated_characters(text: str) -> bool:
    text_lower = text.lower()
    seen_chars = set()
    for char in text_lower:
        if char not in seen_chars:
            seen_chars.add(char)
        else:
            return True
    return False
if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "Python Programming",
        "abcdefg"
    ]
    for s in sample_strings:
        result = has_repeated_characters(s)
        print(f"'{s}' contains repeated characters: {result}")