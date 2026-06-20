def capitalize_first_letter(text):
    if not text:
        return text
    return text[0].upper() + text[1:]

if __name__ == '__main__':
    test_cases = [
        "hello world",
        "123abc",
        "already Capitalized",
        "a",
        "",
        "mixed CASE string"
    ]
    for case in test_cases:
        result = capitalize_first_letter(case)
        print(result)