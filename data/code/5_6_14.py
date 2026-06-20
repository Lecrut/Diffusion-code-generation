def capitalize_first_letter(text):
    if not text:
        return text
    if len(text) == 1:
        return text.upper()
    first_char = text[0]
    if not first_char.isupper():
        if first_char.islower():
            return first_char.upper() + text[1:]
        else:
            return first_char + text[1:]
    return text[0] + text[1:]

if __name__ == '__main__':
    test_cases = ["hello", "HELLO", "123abc", "αβγ", "a", "", "A"]
    for case in test_cases:
        result = capitalize_first_letter(case)
        print(f"{case} -> {result}")