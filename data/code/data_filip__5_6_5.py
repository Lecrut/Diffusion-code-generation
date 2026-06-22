def capitalize_first_char(s):
    if not s:
        return ""
    first = s[0].upper()
    if len(s) == 1:
        return first
    return first + s[1:]

if __name__ == '__main__':
    test_values = ["hello", "HELLO", "", "a", "Äpple", "123abc", " test", "ñ"]
    for value in test_values:
        result = capitalize_first_char(value)
        print(result)