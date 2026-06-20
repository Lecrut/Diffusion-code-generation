def capitalize_first_letter(text):
    if not text:
        return text
    return text[0].upper() + text[1:]

if __name__ == '__main__':
    test_strings = [
        "hello world",
        "python programming",
        "123 numbers",
        "already Capitalized",
        "",
        "a",
        "UPPERCASE START",
        "lowercase start"
    ]
    for s in test_strings:
        print(capitalize_first_letter(s))