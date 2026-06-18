def check_repeated_characters(text):
    text_lower = text.lower()
    char_set = set()
    for char in text_lower:
        if char in char_set:
            return True
        char_set.add(char)
    return False
if __name__ == '__main__':
    sample_strings = [
        "hello",
        "abcdefg",
        "The Quick Brown Fox"
    ]
    for s in sample_strings:
        result = check_repeated_characters(s)
        print(f"'{s}': {'Repeated characters found' if result else 'No repeated characters'}")