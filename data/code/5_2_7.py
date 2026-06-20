def capitalize_first_letter(text):
    if not text:
        return text
    if len(text) == 1:
        return text.upper()
    return text[0].upper() + text[1:]

if __name__ == '__main__':
    test_cases = [
        ("hello world", "Hello world"),
        ("python is great", "Python is great"),
        ("", ""),
        ("a", "A"),
        ("  spaces at start", "  Spaces at start"),
    ]
    for input_val, expected in test_cases:
        result = capitalize_first_letter(input_val)
        if result != expected:
            print(f"Failed: input={input_val}, expected={expected}, got={result}")
        else:
            print(f"Passed: input={input_val}, result={result}")