def capitalize_first_alphanumeric(s):
    if not s:
        return s
    for i, char in enumerate(s):
        if char.isalnum():
            new_char = char.upper()
            if char == new_char:
                break
            return new_char + s[i + 1:]
    return s

if __name__ == '__main__':
    examples = ["hello", "123world", "   test", "!@#abc", "   ", "", "aBc"]
    for text in examples:
        result = capitalize_first_alphanumeric(text)
        print(f"Input: '{text}' -> Output: '{result}'")