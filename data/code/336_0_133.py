def has_repeated_chars(text: str) -> bool:
    text_lower = text.lower()
    char_set = set()
    for ch in text_lower:
        if ch not in ' ':
            if ch in char_set:
                return True
            char_set.add(ch)
    return False
if __name__ == '__main__':
    sample_strings = [
        "hello",
        "abcdefg",
        "Hello World!",
        "Python Programming"
    ]
    for s in sample_strings:
        result = has_repeated_chars(s)
        print(f"'{s}' contains repeated characters: {result}")