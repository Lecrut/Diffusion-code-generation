def capitalize_first_letter(sentence):
    if not sentence:
        return sentence
    return sentence[0].upper() + sentence[1:]

if __name__ == '__main__':
    test_cases = [
        "hello world",
        "HELLO WORLD",
        "hELLO wORLD",
        "",
        "a",
        "123 test",
    ]
    for case in test_cases:
        print(capitalize_first_letter(case))