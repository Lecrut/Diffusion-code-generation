def remove_spaces(input_string):
    WHITESPACE_CHARS = (' ', '\t', '\n', '\r')
    result = input_string
    for char in WHITESPACE_CHARS:
        result = result.replace(char, '')
    return result
if __name__ == '__main__':
    sample_input = 'Here is a \tsample string with \nvarious types of spaces.\r'
    result = remove_spaces(sample_input)
    print(result)