def capitalize_first_letter(text):
    if not text:
        return text
    return text[0].upper() + text[1:]

if __name__ == '__main__':
    test_strings = ["hello world", "123abc", "", "a", "already Capitalized", "mIxEd CaSe sTrInG"]
    for s in test_strings:
        result = capitalize_first_letter(s)
        print(f"{repr(s)} -> {repr(result)}")