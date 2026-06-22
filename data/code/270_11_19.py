def remove_consecutive_spaces(input_string):
    result = []
    in_space_sequence = False
    for char in input_string:
        if char.isspace():
            if not in_space_sequence:
                result.append(char)
                in_space_sequence = True
        else:
            result.append(char)
            in_space_sequence = False
    return ''.join(result)

if __name__ == '__main__':
    test_string1 = "Hello World"
    expected1 = "Hello World"
    result1 = remove_consecutive_spaces(test_string1)
    print(f"Input: '{test_string1}', Result: '{result1}', Expected: '{expected1}'")
    
    test_string2 = "  This is a test \n with spaces. "
    expected2 = "This is a test\nwith spaces."
    result2 = remove_consecutive_spaces(test_string2)
    print(f"Input: '{test_string2}', Result: '{result2}', Expected: '{expected2}'")
    
    test_string3 = "NoSpaces"
    expected3 = "NoSpaces"
    result3 = remove_consecutive_spaces(test_string3)
    print(f"Input: '{test_string3}', Result: '{result3}', Expected: '{expected3}'")