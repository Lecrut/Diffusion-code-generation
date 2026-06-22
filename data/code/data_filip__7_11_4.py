def has_no_special_chars(s):
    for char in s:
        if not char.isalnum():
            return False
    return True

if __name__ == '__main__':
    test_string_1 = "HelloWorld123"
    test_string_2 = "Hello@World"
    print(has_no_special_chars(test_string_1))
    print(has_no_special_chars(test_string_2))