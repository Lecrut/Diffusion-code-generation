def remove_whitespace(s):
    return ''.join(s.split())

if __name__ == '__main__':
    sample_string = "  This is a   test string. "
    result = remove_whitespace(sample_string)
    print(result)