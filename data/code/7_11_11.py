def has_no_special_characters(s: str) -> bool:
    for char in s:
        if not char.isalnum():
            return False
    return True

if __name__ == '__main__':
    test_string_1 = "HelloWorld123"
    test_string_2 = "Hello@World!"
    test_string_3 = "Python3"
    test_string_4 = "C++"
    
    print(has_no_special_characters(test_string_1))
    print(has_no_special_characters(test_string_2))
    print(has_no_special_characters(test_string_3))
    print(has_no_special_characters(test_string_4))