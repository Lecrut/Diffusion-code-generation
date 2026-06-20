def capitalize_first_letter(s):
    if not s:
        return s
    if len(s) == 1:
        return s.upper()
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    sample_strings = ["hello world", "PYTHON", "a", "", "123abc", "mIxEd CaSe"]
    for text in sample_strings:
        result = capitalize_first_letter(text)
        print(result)