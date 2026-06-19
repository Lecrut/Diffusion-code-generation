def remove_all_spaces(input_string):
    return ''.join(input_string.split())

if __name__ == '__main__':
    sample_input = "  This is a \t test string with\n various spaces.  "
    result = remove_all_spaces(sample_input)
    print(result)