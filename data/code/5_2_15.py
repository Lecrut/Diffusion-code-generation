def capitalize_first_letter(text):
    if not text:
        return text
    return text[0].upper() + text[1:]

if __name__ == '__main__':
    test_cases = [
        ("hello world", "Hello world"),
        ("python scripting", "Python scripting"),
        ("", ""),
        ("a", "A"),
        ("already Capitalized", "Already Capitalized"),
        ("123 numbers", "123 numbers"),
    ]
    for input_text, expected_output in test_cases:
        result = capitalize_first_letter(input_text)
        print(result)