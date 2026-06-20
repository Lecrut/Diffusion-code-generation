def capitalize_first_letter(text):
    if not text:
        return text
    return text[0].upper() + text[1:]

if __name__ == '__main__':
    test_strings = [
        "hello world",
        "PYTHON is fun",
        "123 abc",
        "",
        "a",
        "already Capitalized"
    ]
    for s in test_strings:
        result = capitalize_first_letter(s)
        print(result)