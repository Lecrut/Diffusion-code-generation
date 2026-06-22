def remove_whitespace(input_string):
    return ''.join(input_string.split())

if __name__ == '__main__':
    SAMPLE_INPUT = "  This is a   test string with \t various \n whitespace characters.  "
    result = remove_whitespace(SAMPLE_INPUT)
    print(result)