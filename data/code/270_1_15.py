def remove_all_spaces(input_string):
    return input_string.replace(" ", "")

if __name__ == '__main__':
    test_string1 = "Hello World! How are you?"
    result1 = remove_all_spaces(test_string1)
    print(f"Original: '{test_string1}'")
    print(f"Result: '{result1}'")
    
    test_string2 = "   This has\tmultiple\nspaces.  "
    result2 = remove_all_spaces(test_string2)
    print(f"Original: '{test_string2}'")
    print(f"Result: '{result2}'")
    
    test_string3 = "NoSpacesHere"
    result3 = remove_all_spaces(test_string3)
    print(f"Original: '{test_string3}'")
    print(f"Result: '{result3}'")