SPACE_REMOVAL_CHAR = ''

def remove_spaces(input_string):
    return input_string.replace(' ', SPACE_REMOVAL_CHAR)

if __name__ == '__main__':
    sample_input = '  This is   an example string with spaces.  '
    result = remove_spaces(sample_input)
    print(result)