def has_no_special_chars(s):
    for char in s:
        if not char.isalnum():
            return False
    return True

if __name__ == '__main__':
    sample1 = "HelloWorld123"
    sample2 = "Hello World!"
    sample3 = "Test@2024"
    sample4 = "PythonIsGreat"

    print(has_no_special_chars(sample1))
    print(has_no_special_chars(sample2))
    print(has_no_special_chars(sample3))
    print(has_no_special_chars(sample4))