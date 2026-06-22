def check_special_characters(text):
    special_chars = []
    for char in text:
        code = ord(char)
        if code >= 33 and code <= 47 or code >= 58 and code <= 64 or code >= 91 and code <= 96 or code >= 123 and code <= 126:
            special_chars.append(char)
    return special_chars

if __name__ == '__main__':
    sample_text = "Hello, World! 123@456#789"
    result = check_special_characters(sample_text)
    print(result)