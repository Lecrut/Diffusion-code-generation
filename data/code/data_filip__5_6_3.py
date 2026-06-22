def capitalize_first_char(text):
    if not text:
        return text
    return text[0].upper() + text[1:]

if __name__ == '__main__':
    test_values = [
        "hello",
        "HELLO",
        "h",
        "",
        "café",
        "123abc",
        "ß",
        "Ñoño"
    ]
    for value in test_values:
        result = capitalize_first_char(value)
        print(result)