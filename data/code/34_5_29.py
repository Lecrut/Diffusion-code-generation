def capitalize_first_letter(s):
    if not s:
        return ""
    elif len(s) == 1:
        return s.upper()
    else:
        return s[0].upper() + s[1:]

if __name__ == '__main__':
    test_strings = ["hello", "world!", "", "a", "python3.8"]
    for test in test_strings:
        print(capitalize_first_letter(test))