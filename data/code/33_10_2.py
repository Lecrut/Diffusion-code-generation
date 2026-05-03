import string
def remove_all_spaces(input_string):
    return "".join(char for char in input_string if not char.isspace())
if __name__ == '__main__':
    test_string_1 = "Hello World\tThis has\nmultiple spaces"
    expected_output_1 = "HelloWorldThishasmultiplespaces"
    result_1 = remove_all_spaces(test_string_1)
    print(f"Input: '{test_string_1}'")
    print(f"Output: '{result_1}'")
    print(f"Match: {result_1 == expected_output_1}")
    test_string_2 = "NoSpacesHere"
    expected_output_2 = "NoSpacesHere"
    result_2 = remove_all_spaces(test_string_2)
    print(f"\nInput: '{test_string_2}'")
    print(f"Output: '{result_2}'")
    print(f"Match: {result_2 == expected_output_2}")
    test_string_3 = " \t\n"
    expected_output_3 = ""
    result_3 = remove_all_spaces(test_string_3)
    print(f"\nInput: '{test_string_3}'")
    print(f"Output: '{result_3}'")
    print(f"Match: {result_3 == expected_output_3}")