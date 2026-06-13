def split_string_by_spaces(input_string):
    return input_string.split()
if __name__ == '__main__':
    test_string1 = "  hello   world \t python "
    result1 = split_string_by_spaces(test_string1)
    print(result1)
    test_string2 = "singleword"
    result2 = split_string_by_spaces(test_string2)
    print(result2)
    test_string3 = "\t\n multiple\tspaces"
    result3 = split_string_by_spaces(test_string3)
    print(result3)
    test_string4 = ""
    result4 = split_string_by_spaces(test_string4)
    print(result4)