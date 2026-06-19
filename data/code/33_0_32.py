def remove_all_spaces(input_string):
    return ''.join(input_string.split())

if __name__ == '__main__':
    sample_string = "  This is a   test string with various spaces.  "
    result = remove_all_spaces(sample_string)
    print(result)