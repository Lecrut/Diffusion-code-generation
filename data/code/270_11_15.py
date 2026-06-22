def remove_consecutive_spaces(input_string):
    return ' '.join(input_string.split())

if __name__ == '__main__':
    test_string1 = "Hello World"
    expected1 = "Hello World"
    result1 = remove_consecutive_spaces(test_string1)
    print(f"Input: '{test_string1}', Result: '{result1}', Expected: '{expected1}'")
    
    test_string2 = "  This is a test \n with spaces. "
    expected2 = "This is a test with spaces."
    result2 = remove_consecutive_spaces(test_string2)
    print(f"Input: '{test_string2}', Result: '{result2}', Expected: '{expected2}'")
    
    test_string3 = "NoSpaces"
    expected3 = "NoSpaces"
    result3 = remove_consecutive_spaces(test_string3)
    print(f"Input: '{test_string3}', Result: '{result3}', Expected: '{expected3}'")