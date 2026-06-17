import string
def remove_all_spaces(input_string):
    result = ""
    for char in input_string:
        if not char.isspace():
            result += char
    return result
if __name__ == '__main__':
    test_string1 = "Hello World"
    expected1 = "HelloWorld"
    actual1 = remove_all_spaces(test_string1)
    print(f"Input: '{test_string1}'")
    print(f"Output: '{actual1}'")
    print(f"Expected: '{expected1}'")
    print(f"Match: {actual1 == expected1}\n")
    test_string2 = "  This is a test \t with various spaces. "
    expected2 = "Thisisatestwithvariousspaces."
    actual2 = remove_all_spaces(test_string2)
    print(f"Input: '{test_string2}'")
    print(f"Output: '{actual2}'")
    print(f"Expected: '{expected2}'")
    print(f"Match: {actual2 == expected2}\n")
    test_string3 = "NoSpacesHere"
    expected3 = "NoSpacesHere"
    actual3 = remove_all_spaces(test_string3)
    print(f"Input: '{test_string3}'")
    print(f"Output: '{actual3}'")
    print(f"Expected: '{expected3}'")
    print(f"Match: {actual3 == expected3}\n")