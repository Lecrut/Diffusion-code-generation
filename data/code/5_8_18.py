def capitalize_first_letter(text):
    if not text:
        return text
    return text[0].upper() + text[1:]

if __name__ == '__main__':
    test_cases = ["hello", "world", "a", "", "123abc", " already Capitalized"]
    for case in test_cases:
        assert capitalize_first_letter(case) == (case[0].upper() + case[1:]) if case else case
        result = capitalize_first_letter(case)
        print(f"Input: '{case}' -> Output: '{result}'")