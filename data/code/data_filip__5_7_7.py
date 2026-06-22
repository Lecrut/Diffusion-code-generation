def capitalize_first_letter(s):
    if not s:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    test_strings = [
        "hello world",
        "already Capitalized",
        "123 numbers start",
        "",
        "a",
        "UPPERCASE TEST"
    ]
    for test in test_strings:
        print(capitalize_first_letter(test))