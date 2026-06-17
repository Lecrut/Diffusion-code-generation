def check_repeated_chars(text: str) -> bool:
    text_lower = text.lower()
    return len(set(text_lower)) != len(text_lower)
if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "Python Programming",
        "abcdef"
    ]
    for s in sample_strings:
        result = check_repeated_chars(s)
        print(f"'{s}' contains repeated characters: {result}")