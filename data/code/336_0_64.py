def check_repeated_characters(text: str) -> bool:
    text_lower = text.lower()
    char_set = set()
    for char in text_lower:
        if not char.isalnum():                                                                                                                                              
            continue
        if char in char_set:
            return True
        char_set.add(char)
    return False
if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "Python Programming",
        "abcdefg"
    ]
    for s in sample_strings:
        result = check_repeated_characters(s)
        if result:
            print(f"'{s}' contains repeated characters.")
        else:
            print(f"'{s}' has no repeated characters.")