def has_repeated_characters(text):
    text_lower = text.lower()
    char_set = set()
    for char in text_lower:
        if char not in char_set and len(char) == 1:
            char_set.add(char)
        else:
            return True
    return False
if __name__ == '__main__':
    sample_strings = [
        "hello",
        "abcdefg",
        "The Quick Brown Fox Jumps Over The Lazy Dog"
    ]
    for s in sample_strings:
        result = has_repeated_characters(s)
        print(f"'{s}' contains repeated characters: {result}")