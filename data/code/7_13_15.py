def has_special_characters(text):
    for char in text:
        if not (char.isalnum() or char.isspace()):
            return True
    return False

if __name__ == '__main__':
    sample1 = "Hello World"
    sample2 = "Hello, World!"
    sample3 = "12345"
    sample4 = "Test@String"

    print(has_special_characters(sample1))
    print(has_special_characters(sample2))
    print(has_special_characters(sample3))
    print(has_special_characters(sample4))