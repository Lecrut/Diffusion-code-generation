def contains_special_characters(text):
    special_chars = set()
    for char in text:
        code = ord(char)
        if 32 < code < 48 or 57 < code < 65 or 90 < code < 97 or 122 < code < 127:
            special_chars.add(char)
    return special_chars

if __name__ == '__main__':
    sample_string = "Hello, World! 123 @2023"
    result = contains_special_characters(sample_string)
    print(result)