def capitalize_first_letter(sentence):
    if not sentence:
        return sentence
    return sentence[0].upper() + sentence[1:]

if __name__ == '__main__':
    test_cases = [
        "hello world",
        "already Capitalized",
        "a",
        "",
        "123abc",
        "   leading spaces"
    ]
    for case in test_cases:
        result = capitalize_first_letter(case)
        print(f"Input: '{case}' -> Output: '{result}'")