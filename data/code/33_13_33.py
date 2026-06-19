def remove_whitespace(input_string):
    return ''.join(input_string.split())

if __name__ == '__main__':
    sample_string = "  This is a   test string with \t various   whitespaces.  "
    result = remove_whitespace(sample_string)
    print(result)