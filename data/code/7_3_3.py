def has_special_characters(text):
    special_chars = set('!@#$%^&*()_+-=[]{}|;:,.<>?/~`')
    return any(char in special_chars for char in text)

if __name__ == '__main__':
    test_string = "Hello World!"
    result = has_special_characters(test_string)
    print(result)