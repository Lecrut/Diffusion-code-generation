def has_special_chars(text):
    for char in text:
        if not char.isalnum() and char != ' ':
            return True
    return False

if __name__ == '__main__':
    sample_strings = ["HelloWorld", "Hello World", "Hello@World", "Test123", "NoSpecial"]
    for s in sample_strings:
        print(has_special_chars(s))