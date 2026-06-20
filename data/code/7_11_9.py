def has_no_special_characters(s):
    return s.isalnum()

if __name__ == '__main__':
    sample1 = "HelloWorld123"
    sample2 = "Hello World!@#"
    sample3 = ""
    sample4 = "1234567890"
    sample5 = "Hello World"

    print(has_no_special_characters(sample1))
    print(has_no_special_characters(sample2))
    print(has_no_special_characters(sample3))
    print(has_no_special_characters(sample4))
    print(has_no_special_characters(sample5))