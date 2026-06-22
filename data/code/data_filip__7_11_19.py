def has_no_special_characters(text):
    return text.isalnum() or text == ""

if __name__ == '__main__':
    print(has_no_special_characters("HelloWorld123"))
    print(has_no_special_characters("Hello World!"))
    print(has_no_special_characters(""))
    print(has_no_special_characters("12345"))
    print(has_no_special_characters("abc_def"))