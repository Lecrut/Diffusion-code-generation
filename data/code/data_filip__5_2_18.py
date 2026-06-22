def capitalize_sentence(sentence):
    if not sentence:
        return sentence
    return sentence[0].upper() + sentence[1:]

if __name__ == '__main__':
    test_cases = [
        ("hello world", "Hello world"),
        ("", ""),
        ("   spaces", "   spaces"),
        ("all lowercase", "All lowercase"),
        ("AlRearly Capitalized", "AlRearly Capitalized"),
        ("123 numbers", "123 numbers"),
        ("special!@# chars", "Special!@# chars"),
        ("lower case again", "Lower case again"),
    ]
    for input_str, expected in test_cases:
        result = capitalize_sentence(input_str)
        assert result == expected, f"Failed for '{input_str}': got '{result}', expected '{expected}'"
    print(capitalize_sentence("python is great"))
    print(capitalize_sentence("deterministic testing works"))
    print(capitalize_sentence(""))
    print(capitalize_sentence("single"))