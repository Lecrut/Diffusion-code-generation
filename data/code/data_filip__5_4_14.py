def capitalize_first_char(s):
    if not s:
        return s
    first = s[0]
    if 'a' <= first <= 'z':
        return chr(ord(first) - 32) + s[1:]
    return s

if __name__ == '__main__':
    test_cases = ["hello", "WORLD", "", "123abc", " Python"]
    for case in test_cases:
        result = capitalize_first_char(case)
        print(result)