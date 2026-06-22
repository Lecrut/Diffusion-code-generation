def to_camel_case(text):
    if not text:
        return text
    parts = text.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    test_cases = [
        ("hello_world", "helloWorld"),
        ("this_is_a_test", "thisIsATest"),
        ("single", "single"),
        ("alreadyCamelCase", "alreadyCamelCase"),
        ("snake_case_input", "snakeCaseInput"),
        ("", ""),
        ("a_b_c", "aBC"),
    ]
    
    for input_val, expected in test_cases:
        result = to_camel_case(input_val)
        assert result == expected, f"Failed for {input_val}: expected {expected}, got {result}"
        print(f"to_camel_case('{input_val}') -> '{result}'")