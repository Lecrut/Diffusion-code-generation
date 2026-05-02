def remove_all_spaces(input_string):
    return "".join(char for char in input_string if not char.isspace())
if __name__ == '__main__':
    test_string_1 = "Hello World\tThis has\nmultiple spaces"
    result_1 = remove_all_spaces(test_string_1)
    print(f"Original: '{test_string_1}'")
    print(f"Result: '{result_1}'")
    test_string_2 = "NoSpacesHere"
    result_2 = remove_all_spaces(test_string_2)
    print(f"Original: '{test_string_2}'")
    print(f"Result: '{result_2}'")
    test_string_3 = " \t\n"
    result_3 = remove_all_spaces(test_string_3)
    print(f"Original: '{test_string_3}'")
    print(f"Result: '{result_3}'")