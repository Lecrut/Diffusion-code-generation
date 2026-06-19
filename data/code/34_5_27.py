def capitalize_first_letter(s):
    if not s:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    test_cases = [
        "",
        "hello",
        "HELLO",
        "hELLo",
        "hello world",
        "hello, world!",
        "123abc",
        "123ABC",
        "123aBC"
    ]
    
    for case in test_cases:
        print(capitalize_first_letter(case))