def capitalize_first_letter(s):
    if not s:
        return ""
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    test_cases = [
        "",
        "hello",
        "world!",
        "123abc",
        "already Capitalized",
        "punctuation, should stay: .!?"
    ]
    
    for case in test_cases:
        print(capitalize_first_letter(case))