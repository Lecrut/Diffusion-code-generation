def remove_whitespace(input_string):
    return ''.join(input_string.split())

if __name__ == '__main__':
    sample_string = "  This is a   sample string with \t various \n whitespace characters.  "
    result = remove_whitespace(sample_string)
    print(result)