def has_special_characters(text):
    return any(not c.isalnum() and not c.isspace() for c in text)

if __name__ == '__main__':
    print(has_special_characters("Hello World"))
    print(has_special_characters("Hello World!"))
    print(has_special_characters("12345"))
    print(has_special_characters("abc@def"))