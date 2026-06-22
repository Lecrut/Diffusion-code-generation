def remove_all_spaces(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    return input_string.replace(' ', '')

if __name__ == '__main__':
    test_string_1 = "Hello World! How are you?"
    print(f"Original: '{test_string_1}'")
    print(f"Result: '{remove_all_spaces(test_string_1)}'")
    
    test_string_2 = "   This has\tmultiple\nspaces.  "
    print(f"Original: '{test_string_2}'")
    print(f"Result: '{remove_all_spaces(test_string_2)}'")
    
    test_string_3 = "NoSpacesHere"
    print(f"Original: '{test_string_3}'")
    print(f"Result: '{remove_all_spaces(test_string_3)}'")