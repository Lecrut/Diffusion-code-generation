def get_char_list(s):
    return list(s)
if __name__ == '__main__':
    test_string_1 = "hello"
    result_1 = get_char_list(test_string_1)
    print(f"Input: '{test_string_1}', Output: {result_1}")
    test_string_2 = ""
    result_2 = get_char_list(test_string_2)
    print(f"Input: '{test_string_2}', Output: {result_2}")
    test_string_3 = "Python"
    result_3 = get_char_list(test_string_3)
    print(f"Input: '{test_string_3}', Output: {result_3}")
    test_string_4 = "12345"
    result_4 = get_char_list(test_string_4)
    print(f"Input: '{test_string_4}', Output: {result_4}")