def capitalize_first(s):
    if not s:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    test_strings = ["hello", "WORLD", "hello world", "", "a", "123abc"]
    for test in test_strings:
        print(capitalize_first(test))