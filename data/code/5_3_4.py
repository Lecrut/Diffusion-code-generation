def capitalize_first_if_alnum(s):
    if not s:
        return s
    first_char = s[0]
    if first_char.isalnum():
        return first_char.upper() + s[1:]
    return s

if __name__ == '__main__':
    test_cases = [
        "hello world",
        "123abc",
        "!@#test",
        "already Capitalized",
        "",
        "42",
        " a"
    ]
    for case in test_cases:
        print(capitalize_first_if_alnum(case))