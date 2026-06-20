def capitalize_first_letter(s):
    if not s:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    test_cases = [
        "hello",
        "world",
        "a",
        "",
        "123abc",
        "café",
        "über",
        "日本語",
        "αβγ",
        "  spaced",
    ]
    for case in test_cases:
        result = capitalize_first_letter(case)
        print(f"Input: {repr(case)} -> Output: {repr(result)}")