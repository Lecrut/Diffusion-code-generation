def capitalize_first(text):
    if not text:
        return text
    return text[0].upper() + text[1:]

if __name__ == '__main__':
    test_strings = ["hello", "python", "world", "", "a"]
    for s in test_strings:
        print(capitalize_first(s))