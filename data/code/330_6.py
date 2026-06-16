def capitalize_string(input_string):
    if not input_string:
        return ""
    return input_string.upper()
if __name__ == '__main__':
    test_cases = [
        ("", ""),
        ("hello", "HELLO"),
        ("world", "WORLD"),
        ("MiXeD CaSe", "MIXED CASE"),
        ("ALL CAPS", "ALL CAPS")
    ]
    for input_str, expected_output in test_cases:
        actual_output = capitalize_string(input_str)
        assert actual_output == expected_output, f"Input: '{input_str}', Expected: '{expected_output}', Got: '{actual_output}'"
        print(f"Test passed for input: '{input_str}'")