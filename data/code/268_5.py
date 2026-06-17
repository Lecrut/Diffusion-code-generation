def find_first_word(text):
    if not text or text.isspace():
        return ""
    words = text.split()
    if words:
        return words[0]
    else:
        return ""
if __name__ == '__main__':
    test_cases = [
        ("", ""),
        ("   ", ""),
        ("hello world", "hello"),
        ("  leading space", "leading"),
        ("trailing space ", "trailing"),
        ("singleword", "singleword"),
        ("", ""),
        ("   ", "")
    ]
    for input_str, expected in test_cases:
        result = find_first_word(input_str)
        assert result == expected, f"Input: '{input_str}', Expected: '{expected}', Got: '{result}'"
        print(f"Input: '{input_str}', Result: '{result}' (Passed)")