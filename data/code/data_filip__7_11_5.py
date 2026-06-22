def has_no_special_characters(text):
    if not text:
        return True
    for char in text:
        if not char.isalnum() and not char.isspace():
            return False
    return True

if __name__ == '__main__':
    sample1 = "HelloWorld"
    sample2 = "Hello World!"
    sample3 = "12345"
    sample4 = "test@example"
    print(has_no_special_characters(sample1))
    print(has_no_special_characters(sample2))
    print(has_no_special_characters(sample3))
    print(has_no_special_characters(sample4))