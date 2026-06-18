def check_repeated_chars(text: str) -> bool:
    text_lower = text.lower()
    char_set = set()
    for char in text_lower:
        if char not in char_set and len(char) == 1:
            char_set.add(char)
        else:
            return True
    return False
if __name__ == '__main__':
    sample_strings = ["hello", "abcdefg", "aaaaa"]
    for s in sample_strings:
        result = check_repeated_chars(s)
        if result:
            print(f"'{s}' contains repeated characters.")
        else:
            print(f"'{s}' has no repeated characters.")