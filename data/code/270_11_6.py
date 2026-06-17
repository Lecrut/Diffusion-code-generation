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
    print(f"Input: '{test_string1}', Output: '{actual1}', Expected: '{expected1}'")
    test_string2 = "  This is a test \n with spaces. "
    expected2 = "Thisisatestwithspaces."
    actual2 = remove_all_spaces(test_string2)
    print(f"Input: '{test_string2}', Output: '{actual2}', Expected: '{expected2}'")
    test_string3 = "NoSpaces"
    expected3 = "NoSpaces"
    actual3 = remove_all_spaces(test_string3)
    print(f"Input: '{test_string3}', Output: '{actual3}', Expected: '{expected3}'")
    test_string4 = " \t\n"
    expected4 = ""
    actual4 = remove_all_spaces(test_string4)
    print(f"Input: '{test_string4}', Output: '{actual4}', Expected: '{expected4}'")