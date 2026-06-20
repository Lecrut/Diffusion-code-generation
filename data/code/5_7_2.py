def capitalize_first_letter(text):
    if not text:
        return text
    return text[0].upper() + text[1:]

if __name__ == '__main__':
    test_strings = [
        "hello world",
        "PYTHON IS GREAT",
        "mixedCase string",
        "123 numbers start",
        "!special char start",
        ""
    ]
    
    for s in test_strings:
        result = capitalize_first_letter(s)
        print(result)