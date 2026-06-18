def check_repeated_chars(text: str) -> bool:
    text_lower = text.lower()
    char_set = set()
    for char in text_lower:
        if char not in char_set:
            char_set.add(char)
        else:
            return True
    return False
if __name__ == '__main__':
    sample_strings = [
        "hello",
        "abcdefg",
        "The Quick Brown Fox"
    ]
    for s in sample_strings:
        result = check_repeated_chars(s)
        print(f"'{s}': {'Contains repeated characters' if result else 'No repeated characters'}")