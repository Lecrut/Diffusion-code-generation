def minify_text(input_string):
    return ''.join(input_string.split())

if __name__ == '__main__':
    sample_input = "  This is   a sample string with \t various   whitespaces.  "
    result = minify_text(sample_input)
    print(result)