def remove_all_spaces(input_string):
    result = ""
    for char in input_string:
        if not char.isspace():
            result += char
    return result
if __name__ == '__main__':
    test_string1 = "Hello World"
    expected1 = "HelloWorld"
    result1 = remove_all_spaces(test_string1)
    print(f"Input: '{test_string1}', Result: '{result1}', Expected: '{expected1}'")
    test_string2 = "  This has   many spaces \t"
    expected2 = "Thishasmanyspaces"
    result2 = remove_all_spaces(test_string2)
    print(f"Input: '{test_string2}', Result: '{result2}', Expected: '{expected2}'")
    test_string3 = "NoSpaces"
    expected3 = "NoSpaces"
    result3 = remove_all_spaces(test_string3)
    print(f"Input: '{test_string3}', Result: '{result3}', Expected: '{expected3}'")
    test_string4 = ""
    expected4 = ""
    result4 = remove_all_spaces(test_string4)
    print(f"Input: '{test_string4}', Result: '{result4}', Expected: '{expected4}'")