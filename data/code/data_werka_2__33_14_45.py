def remove_spaces(input_string):
    return ''.join(input_string.split())

if __name__ == '__main__':
    sample_input = "  This is   an example string with spaces.  "
    result = remove_spaces(sample_input)
    print(result)