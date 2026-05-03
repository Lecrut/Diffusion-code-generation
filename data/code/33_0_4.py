def remove_all_spaces(input_string):
    return input_string.replace(' ', '').replace('\t', '').replace('\n', '').replace('\r', '')
if __name__ == '__main__':
    test_string_1 = "Hello World\tHow are you?\n"
    result_1 = remove_all_spaces(test_string_1)
    print(f"Original: '{test_string_1}'")
    print(f"Result: '{result_1}'")
    test_string_2 = "   This has\tmultiple\nspaces. "
    result_2 = remove_all_spaces(test_string_2)
    print(f"Original: '{test_string_2}'")
    print(f"Result: '{result_2}'")
    test_string_3 = "NoSpacesHere"
    result_3 = remove_all_spaces(test_string_3)
    print(f"Original: '{test_string_3}'")
    print(f"Result: '{result_3}'")