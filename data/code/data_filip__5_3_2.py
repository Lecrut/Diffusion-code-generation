def capitalize_first_if_alnum(s: str) -> str:
    if not s:
        return s
    first_char = s[0]
    if not first_char.isalnum():
        return s
    return first_char.upper() + s[1:]

if __name__ == '__main__':
    test_cases = [
        "hello world",
        "123abc",
        "!hello",
        "   spaces",
        "ABC",
        "",
        "a1b2c3"
    ]
    for case in test_cases:
        result = capitalize_first_if_alnum(case)
        print(f"Input: '{case}' -> Output: '{result}'")