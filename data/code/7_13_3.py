def has_special_characters(s):
    for char in s:
        if not (char.isalnum() or char == ' '):
            return True
    return False

if __name__ == '__main__':
    print(has_special_characters("Hello World"))
    print(has_special_characters("Hello, World!"))
    print(has_special_characters("123 456"))
    print(has_special_characters("abc def"))
    print(has_special_characters("!@#$%"))