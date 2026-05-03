import string
def remove_all_spaces(input_string):
    return "".join(char for char in input_string if not char.isspace())
if __name__ == '__main__':
    test_string_1 = "Hello World\t\nThis has spaces."
    result_1 = remove_all_spaces(test_string_1)
    print(f"Input: '{test_string_1}'")
    print(f"Output: '{result_1}'")
    test_string_2 = "NoSpacesHere"
    result_2 = remove_all_spaces(test_string_2)
    print(f"Input: '{test_string_2}'")
    print(f"Output: '{result_2}'")
    test_string_3 = " \t\n"
    result_3 = remove_all_spaces(test_string_3)
    print(f"Input: '{test_string_3}'")
    print(f"Output: '{result_3}'")