def has_special_characters(text):
    for char in text:
        if not (char.isalnum() or char.isspace()):
            return True
    return False

if __name__ == '__main__':
    print(has_special_characters("Hello World"))
    print(has_special_characters("Hello, World!"))
    print(has_special_characters("   "))
    print(has_special_characters("12345"))
    print(has_special_characters("@#$"))