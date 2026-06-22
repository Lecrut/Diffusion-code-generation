def capitalize_first(s):
    if not s:
        return s
    first_char = s[0]
    if first_char.islower():
        return first_char.upper() + s[1:]
    return s

if __name__ == '__main__':
    test_values = ["hello", "HELLO", "h", "", "ñino", "123abc", "Äpfel"]
    for value in test_values:
        print(capitalize_first(value))