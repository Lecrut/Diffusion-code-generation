def remove_whitespace(s):
    return ''.join(s.split())

if __name__ == '__main__':
    sample_string = "  This is a   test string with \t various \n whitespace characters.  "
    result = remove_whitespace(sample_string)
    print(result)