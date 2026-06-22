def capitalize_first_letter(sentence):
    if not sentence:
        return sentence
    if not sentence[0].isalpha():
        return sentence
    return sentence[0].upper() + sentence[1:]

if __name__ == '__main__':
    test_cases = [
        "hello world",
        "PYTHON is great",
        "123 start",
        "",
        "a",
        "already Capitalized",
        "   spaces before"
    ]
    
    for case in test_cases:
        result = capitalize_first_letter(case)
        print(result)