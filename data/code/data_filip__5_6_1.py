def capitalize_first_letter(s):
    if not s:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    test_cases = [
        "hello",
        "h",
        "",
        "world",
        "café",
        "über",
        "πi",
        "123abc",
        "   spaced",
        "ALREADY Capitalized"
    ]

    for test in test_cases:
        result = capitalize_first_letter(test)
        print(repr(result))