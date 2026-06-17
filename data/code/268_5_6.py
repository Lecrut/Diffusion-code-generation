def find_first_word(text):
    if not text:
        return ""
    stripped_text = text.lstrip()
    if not stripped_text:
        return ""
    first_word = ""
    for char in stripped_text:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            first_word += char
        else:
            break
    return first_word
if __name__ == '__main__':
    test_cases = [
        ("", ""),
        ("   ", ""),
        ("hello world", "hello"),
        ("  python programming", "python"),
        ("   ", ""),
        ("   ", ""),
        ("a", "a"),
        ("  \t\n", ""),
        ("  leading space", "leading"),
        ("", "")
    ]
    for input_str, expected in test_cases:
        result = find_first_word(input_str)
        assert result == expected, f"Input: '{input_str}', Expected: '{expected}', Got: '{result}'"
        print(f"Input: '{input_str}', Result: '{result}', Passed")