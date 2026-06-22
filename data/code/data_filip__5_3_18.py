def capitalize_first_alnum(s):
    if not s:
        return s
    first_char = s[0]
    if not first_char.isalnum():
        return s
    return first_char.upper() + s[1:]

if __name__ == '__main__':
    test_cases = ["hello world", "123abc", "!important", "", "aBc", "1b2c", "!!!test", "Zebra"]
    for text in test_cases:
        result = capitalize_first_alnum(text)
        print(f"Input: '{text}' -> Output: '{result}'")