def remove_all_spaces(input_string):
    return input_string.replace(' ', '').replace('\t', '').replace('\n', '').replace('\r', '')
if __name__ == '__main__':
    test_string_1 = "Hello World\nThis has\tmultiple spaces."
    result_1 = remove_all_spaces(test_string_1)
    print(f"Original: {repr(test_string_1)}")
    print(f"Result: {repr(result_1)}")
    test_string_2 = "   leading and trailing spaces   "
    result_2 = remove_all_spaces(test_string_2)
    print(f"Original: {repr(test_string_2)}")
    print(f"Result: {repr(result_2)}")
    test_string_3 = "NoSpaces"
    result_3 = remove_all_spaces(test_string_3)
    print(f"Original: {repr(test_string_3)}")
    print(f"Result: {repr(result_3)}")