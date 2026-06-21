def remove_whitespace(input_string):
    return ''.join(input_string.split())

if __name__ == '__main__':
    sample_input = "  This is a sample string with   various   whitespaces.  "
    result = remove_whitespace(sample_input)
    print(result)