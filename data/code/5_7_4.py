def capitalize_first_letter(text):
    if not text:
        return text
    return text[0].upper() + text[1:]

if __name__ == '__main__':
    test_cases = ["hello world", "python is great", "123 abc", "already Capitalized", ""]
    for case in test_cases:
        result = capitalize_first_letter(case)
        print(f"Input: '{case}' -> Output: '{result}'")