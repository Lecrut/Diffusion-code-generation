def split_string_by_spaces(input_str):
    return input_str.split()

if __name__ == '__main__':
    test_str = "Python Programming Split by Spaces"
    result = split_string_by_spaces(test_str)
    print(result)