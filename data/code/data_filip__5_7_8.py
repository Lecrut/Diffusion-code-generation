def capitalize_first(s: str) -> str:
    if not s:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    test_strings = [
        "hello world",
        "python",
        "CAPITAL",
        "mixed Case",
        "",
        "123abc",
        "   spaces"
    ]
    for text in test_strings:
        result = capitalize_first(text)
        print(result)