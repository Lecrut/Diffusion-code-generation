def has_no_special_characters(text):
    if not text:
        return True
    return all((char.isalnum() for char in text))
if __name__ == '__main__':
    sample1 = 'HelloWorld123'
    sample2 = 'Hello World!'
    sample3 = 'NoSpecialCharacters@Here'
    sample4 = ''
    sample5 = 'Python3'
    print(has_no_special_characters(sample1))
    print(has_no_special_characters(sample2))
    print(has_no_special_characters(sample3))
    print(has_no_special_characters(sample4))
    print(has_no_special_characters(sample5))