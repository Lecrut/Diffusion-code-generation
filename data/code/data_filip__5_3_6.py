def capitalize_first_alphanumeric(s: str) -> str:
    if not s:
        return s
    first_char = s[0]
    if not first_char.isalnum():
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    test_cases = ["hello", "123abc", "  spaces", "!special", "world", "123", "", "aBc", "$100"]
    for case in test_cases:
        result = capitalize_first_alphanumeric(case)
        print(f"Input: '{case}' -> Output: '{result}'")