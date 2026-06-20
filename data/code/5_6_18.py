def capitalize_first_char(s):
    if not s:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    test_values = [
        "",
        "a",
        "hello",
        "héllo",
        "αβγ",
        "123abc",
        " already capitalized",
    ]
    for val in test_values:
        print(capitalize_first_char(val))