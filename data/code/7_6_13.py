def has_special_characters(text):
    for char in text:
        if not char.isalnum() and not char.isspace():
            return True
    return False

if __name__ == '__main__':
    print(has_special_characters("Hello World"))
    print(has_special_characters("Hello World!"))
    print(has_special_characters("Test@123"))
    print(has_special_characters("PlainText"))
    print(has_special_characters("  spaces  "))
    print(has_special_characters("special#char"))