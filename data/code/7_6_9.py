def has_special_chars(text):
    for char in text:
        if not char.isalnum() and (not char.isspace()):
            return True
    return False
if __name__ == '__main__':
    print(has_special_chars('Hello World'))
    print(has_special_chars('Hello, World!'))
    print(has_special_chars('Test123'))
    print(has_special_chars('Special@Char'))