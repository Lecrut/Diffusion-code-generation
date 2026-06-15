def get_char_list(s):
    return list(s)
if __name__ == '__main__':
    test_string_1 = "hello"
    expected_1 = ['h', 'e', 'l', 'l', 'o']
    result_1 = get_char_list(test_string_1)
    print(f"Input: '{test_string_1}', Result: {result_1}, Expected: {expected_1}")
    test_string_2 = ""
    expected_2 = []
    result_2 = get_char_list(test_string_2)
    print(f"Input: '{test_string_2}', Result: {result_2}, Expected: {expected_2}")
    test_string_3 = "Python"
    expected_3 = ['P', 'y', 't', 'h', 'o', 'n']
    result_3 = get_char_list(test_string_3)
    print(f"Input: '{test_string_3}', Result: {result_3}, Expected: {expected_3}")
    test_string_4 = "a"
    expected_4 = ['a']
    result_4 = get_char_list(test_string_4)
    print(f"Input: '{test_string_4}', Result: {result_4}, Expected: {expected_4}")