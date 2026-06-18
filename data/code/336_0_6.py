def has_repeated_characters(text: str) -> bool:
    text_lower = text.lower()
    return len(set(text_lower)) != len(text_lower)
if __name__ == '__main__':
    sample_strings = [
        "hello",
        "abcdefg",
        "Hello World!",
        "",
        "a"
    ]
    for s in sample_strings:
        result = has_repeated_characters(s)
        print(f"'{s}' -> {'Has repeated characters' if result else 'No repeated characters'}")