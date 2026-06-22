def has_no_special_characters(s):
    if not s:
        return True
    return s.isalnum() or s.replace(" ", "").isalnum()

if __name__ == '__main__':
    sample1 = "HelloWorld123"
    sample2 = "Hello World!"
    sample3 = "NoSpecialChars"
    print(has_no_special_characters(sample1))
    print(has_no_special_characters(sample2))
    print(has_no_special_characters(sample3))