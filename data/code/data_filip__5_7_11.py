def capitalize_first(s):
    if not s:
        return ""
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    test_strings = ["hello world", "python", "123abc", "", "a"]
    for t in test_strings:
        print(capitalize_first(t))