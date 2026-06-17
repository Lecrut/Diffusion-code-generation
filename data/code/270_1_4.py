def remove_all_spaces(input_string):
    return "".join(char for char in input_string if not char.isspace())
if __name__ == '__main__':
    test_string1 = "Hello World"
    result1 = remove_all_spaces(test_string1)
    print(f"Input: '{test_string1}'")
    print(f"Output: '{result1}'")
    test_string2 = "  This has\tmultiple spaces \n"
    result2 = remove_all_spaces(test_string2)
    print(f"Input: '{test_string2.replace(' ', ' ').replace('\t', '\\t').replace('\n', '\\n')}'")
    print(f"Output: '{result2}'")
    test_string3 = "NoSpacesHere"
    result3 = remove_all_spaces(test_string3)
    print(f"Input: '{test_string3}'")
    print(f"Output: '{result3}'")