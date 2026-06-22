def capitalize_first(s):
    if not s:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    test_cases = ["hello", "HELLO", "h", "", "café", "Ñoño", "123abc", " a"]
    for text in test_cases:
        result = capitalize_first(text)
        print(f"Input: '{text}' -> Output: '{result}'")