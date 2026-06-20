def capitalize_first_if_alphanumeric(s):
    if not s:
        return s
    first_char = s[0]
    if not first_char.isalnum():
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    test_cases = [
        "hello world",
        "123abc",
        "!hello",
        "",
        "Python",
        "99problems",
        ".start_with_dot"
    ]
    for case in test_cases:
        result = capitalize_first_if_alphanumeric(case)
        print(result)