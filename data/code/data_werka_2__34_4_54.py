def capitalize_first_letter(s):
    if not s:
        return ""
    if len(s) == 1 and s[0].isalpha():
        return s.upper()
    first_char = s[0].upper() if s[0].isalpha() else s[0]
    rest_of_string = s[1:]
    return first_char + rest_of_string

if __name__ == '__main__':
    sample_values = [
        "hello world",
        "HELLO WORLD",
        "hello WORLD",
        "hElLo WoRlD",
        "",
        "a",
        "123abc",
        "!@#abc",
        "a!@#bc",
        "12345"
    ]
    for value in sample_values:
        print(capitalize_first_letter(value))