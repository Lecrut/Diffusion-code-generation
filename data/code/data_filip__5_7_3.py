def capitalize_first_letter(text):
    if not text:
        return text
    if len(text) == 1:
        return text.upper()
    return text[0].upper() + text[1:]

if __name__ == '__main__':
    test_strings = ["hello", "world", "123abc", "", "a", "PYTHON", "mixed case here"]
    for s in test_strings:
        result = capitalize_first_letter(s)
        print(result)