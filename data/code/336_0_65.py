def has_repeated_characters(text: str) -> bool:
    char_set = set()
    for char in text.lower():
        if char not in char_set:
            char_set.add(char)
        else:
            return True
    return False
if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "abcdefg",
        "The quick brown fox jumps over the lazy dog"
    ]
    for s in sample_strings:
        result = has_repeated_characters(s)
        print(f"'{s}' contains repeated characters: {result}")