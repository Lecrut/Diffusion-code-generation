def capitalize_first(s):
    if not s:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    test_strings = ["hello", "world", "python", "a", ""]
    for string in test_strings:
        result = capitalize_first(string)
        print(result)