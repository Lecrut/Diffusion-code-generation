def capitalize_first_letter(sentence):
    if not sentence:
        return sentence
    return sentence[0].upper() + sentence[1:]

if __name__ == '__main__':
    test_cases = [
        "hello world",
        "python programming",
        "already Capitalized",
        "",
        "a",
        "123 numbers"
    ]
    for test in test_cases:
        result = capitalize_first_letter(test)
        print(result)