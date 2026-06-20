def has_special_characters(s):
    import string
    special_chars = set(string.punctuation)
    return any(char in special_chars for char in s)

if __name__ == '__main__':
    test_string_1 = "Hello World"
    test_string_2 = "Hello@World!"
    print(has_special_characters(test_string_1))
    print(has_special_characters(test_string_2))