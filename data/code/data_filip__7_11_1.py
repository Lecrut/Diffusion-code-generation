def has_no_special_characters(text):
    return text.isalnum() or text == ""

if __name__ == '__main__':
    sample1 = "HelloWorld123"
    sample2 = "Hello World!"
    sample3 = ""
    sample4 = "Test_123"
    print(has_no_special_characters(sample1))
    print(has_no_special_characters(sample2))
    print(has_no_special_characters(sample3))
    print(has_no_special_characters(sample4))