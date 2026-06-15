import string
def remove_all_spaces(input_string):
    result = ""
    for char in input_string:
        if not char.isspace():
            result += char
    return result
if __name__ == '__main__':
    test_string_1 = "Hello World"
    expected_output_1 = "HelloWorld"
    actual_output_1 = remove_all_spaces(test_string_1)
    print(f"Input: '{test_string_1}'")
    print(f"Output: '{actual_output_1}'")
    print(f"Expected: '{expected_output_1}'")
    print(f"Test 1 Passed: {actual_output_1 == expected_output_1}\n")
    test_string_2 = "  This is a test \t with various spaces\n"
    expected_output_2 = "Thisisatestwithvariousspaces"
    actual_output_2 = remove_all_spaces(test_string_2)
    print(f"Input: '{test_string_2.replace('\\t', ' ')}'")
    print(f"Output: '{actual_output_2}'")
    print(f"Expected: '{expected_output_2}'")
    print(f"Test 2 Passed: {actual_output_2 == expected_output_2}\n")
    test_string_3 = "NoSpacesHere"
    expected_output_3 = "NoSpacesHere"
    actual_output_3 = remove_all_spaces(test_string_3)
    print(f"Input: '{test_string_3}'")
    print(f"Output: '{actual_output_3}'")
    print(f"Expected: '{expected_output_3}'")
    print(f"Test 3 Passed: {actual_output_3 == expected_output_3}\n")