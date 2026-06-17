def check_repeated_characters(text):
    text_lower = text.lower()
    char_set = set()
    for char in text_lower:
        if char not in char_set and len(char) > 0:
            char_set.add(char)
        elif char in char_set:
            return True
    return False
if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "abcdefg",
        "Python Programming"
    ]
    for s in sample_strings:
        result = check_repeated_characters(s)
        if result:
            print(f"'{s}' contains repeated characters.")
        else:
            print(f"'{s}' has no repeated characters.")