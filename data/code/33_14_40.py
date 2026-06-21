SPACE_CHARACTER = ' '

def remove_spaces(input_string):
    return input_string.replace(SPACE_CHARACTER, '')

if __name__ == '__main__':
    sample_input = "  This is   a unique string with various spaces.  "
    result = remove_spaces(sample_input)
    print(result)