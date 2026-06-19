def remove_whitespace(input_string):
    return ''.join(input_string.split())

if __name__ == '__main__':
    sample_string = "  This is   a\tstring with\nvarious   whitespaces.  "
    result = remove_whitespace(sample_string)
    print(result)