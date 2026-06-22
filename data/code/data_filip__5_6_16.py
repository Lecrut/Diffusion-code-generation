def capitalize_first_char(s: str) -> str:
    if not s:
        return s
    first = s[0].upper()
    if len(s) == 1:
        return first
    return first + s[1:]

if __name__ == '__main__':
    test_cases = [
        "",
        "a",
        "hello",
        "HELLO",
        "hELLo",
        "café",
        "Ελληνικά",
        "  space",
        "123abc"
    ]
    for value in test_cases:
        result = capitalize_first_char(value)
        print(result)