def check_repeated_characters(text):
    text_lower = text.lower()
    char_count = {}
    for char in text_lower:
        if not char.isalnum():                                                                                                                                                                             
            continue
        count = char_count.get(char, 0) + 1
        char_count[char] = count
    for char in char_count:
        if char_count[char] > 1:
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