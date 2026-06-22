def remove_all_spaces(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    return input_string.replace(' ', '')

if __name__ == '__main__':
    test_string1 = "Hello World! How are you?"
    result_1 = remove_all_spaces(test_string1)
    print(f"Original: '{test_string1}'")
    print(f"Result: '{result_1}'")
    
    test_string2 = "   This has\tmultiple\nspaces.  "
    result_2 = remove_all_spaces(test_string2)
    print(f"Original: '{test_string2}'")
    print(f"Result: '{result_2}'")
    
    test_string3 = "NoSpacesHere"
    result_3 = remove_all_spaces(test_string3)
    print(f"Original: '{test_string3}'")
    print(f"Result: '{result_3}'")