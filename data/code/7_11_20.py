def has_no_special_characters(s):
    return all(char.isalnum() for char in s) or len(s) == 0

if __name__ == '__main__':
    test_string_1 = "HelloWorld123"
    test_string_2 = "Hello@World"
    test_string_3 = "Python3.11"
    test_string_4 = "ValidName123"
    
    result_1 = has_no_special_characters(test_string_1)
    result_2 = has_no_special_characters(test_string_2)
    result_3 = has_no_special_characters(test_string_3)
    result_4 = has_no_special_characters(test_string_4)
    
    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)