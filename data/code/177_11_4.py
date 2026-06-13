def split_string_by_spaces(text):
    return text.split()
if __name__ == '__main__':
    test_string1 = "  hello   world \t this has multiple spaces "
    result1 = split_string_by_spaces(test_string1)
    print(result1)
    test_string2 = "singleword"
    result2 = split_string_by_spaces(test_string2)
    print(result2)
    test_string3 = "\n\t leading and trailing whitespace \r"
    result3 = split_string_by_spaces(test_string3)
    print(result3)