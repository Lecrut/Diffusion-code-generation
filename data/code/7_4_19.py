def find_first_special_char(s):
    for char in s:
        if not char.isalnum() and not char.isspace():
            return char
    return None

if __name__ == '__main__':
    test_string_1 = "Hello World"
    result_1 = find_first_special_char(test_string_1)
    print(result_1)
    test_string_2 = "Price: $50.00"
    result_2 = find_first_special_char(test_string_2)
    print(result_2)
    test_string_3 = "1234567890"
    result_3 = find_first_special_char(test_string_3)
    print(result_3)