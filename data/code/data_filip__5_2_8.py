def capitalize_first_letter(sentence):
    if not sentence:
        return ""
    return sentence[0].upper() + sentence[1:]

if __name__ == '__main__':
    test_cases = [
        ("hello world", "Hello world"),
        ("python is great", "Python is great"),
        ("", ""),
        ("a", "A"),
        ("123 abc", "123 abc"),
        ("multiple   spaces", "Multiple   spaces"),
    ]
    
    for input_val, expected in test_cases:
        result = capitalize_first_letter(input_val)
        print(f"Input: '{input_val}' -> Output: '{result}' -> Match: {result == expected}")
    
    print(capitalize_first_letter("sample dynamic value"))