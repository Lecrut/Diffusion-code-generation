def split_string_by_spaces(input_string):
    return input_string.split(' ')
if __name__ == '__main__':
    test_string_1 = "hello world"
    result_1 = split_string_by_spaces(test_string_1)
    print(f"Input: '{test_string_1}'")
    print(f"Output: {result_1}")
    test_string_2 = "  leading and trailing spaces "
    result_2 = split_string_by_spaces(test_string_2)
    print(f"Input: '{test_string_2}'")
    print(f"Output: {result_2}")
    test_string_3 = "singleword"
    result_3 = split_string_by_spaces(test_string_3)
    print(f"Input: '{test_string_3}'")
    print(f"Output: {result_3}")
    test_string_4 = ""
    result_4 = split_string_by_spaces(test_string_4)
    print(f"Input: '{test_string_4}'")
    print(f"Output: {result_4}")