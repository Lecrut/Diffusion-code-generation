def capitalize_first_if_alnum(s):
    if not s:
        return s
    if s[0].isalnum():
        return s[0].upper() + s[1:]
    return s

if __name__ == '__main__':
    test_cases = ["hello", "hello world", "123abc", "!hello", "", "  test"]
    for case in test_cases:
        result = capitalize_first_if_alnum(case)
        print(result)