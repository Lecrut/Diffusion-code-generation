def split_string_by_spaces(text):
    return text.split()
if __name__ == '__main__':
    sample_string1 = "  hello   world \t this is a test "
    result1 = split_string_by_spaces(sample_string1)
    print(result1)
    sample_string2 = "singleword"
    result2 = split_string_by_spaces(sample_string2)
    print(result2)
    sample_string3 = "\t\n  "
    result3 = split_string_by_spaces(sample_string3)
    print(result3)