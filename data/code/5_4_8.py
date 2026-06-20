def capitalize_first(s):
    if len(s) == 0:
        return s
    first_char = s[0]
    if 'a' <= first_char <= 'z':
        upper_char = chr(ord(first_char) - 32)
        return upper_char + s[1:]
    return s

if __name__ == '__main__':
    test_cases = ["hello", "world", "Python", "test", "", "123abc", "ABC", "a"]
    for case in test_cases:
        result = capitalize_first(case)
        print(result)