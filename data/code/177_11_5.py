def split_string_by_spaces(text):
    return text.split()
if __name__ == '__main__':
    sample1 = "  hello   world\tthis has multiple spaces "
    result1 = split_string_by_spaces(sample1)
    print(result1)
    sample2 = "singleword"
    result2 = split_string_by_spaces(sample2)
    print(result2)
    sample3 = "\n\t leading and trailing spaces\r"
    result3 = split_string_by_spaces(sample3)
    print(result3)