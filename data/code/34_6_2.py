def capitalize_first_letter_only(text):
    if not text:
        return ""
    result = text[0].upper() + text[1:]
    return result
if __name__ == '__main__':
    test_cases = [
        ("", ""),
        ("hello", "Hello"),
        ("world", "World"),
        ("aBc", "ABc"),
        ("python", "Python"),
        ("", ""),
        ("  leading space", "  leading space"),
        ("!start", "!start"),
        ("end.", "End."),
        ("", "")
    ]
    for input_str, expected_output in test_cases:
        actual_output = capitalize_first_letter_only(input_str)
        assert actual_output == expected_output, f"Input: '{input_str}', Expected: '{expected_output}', Got: '{actual_output}'"
        print(f"Input: '{input_str}' -> Output: '{actual_output}' (Passed)")