def minify_text(input_string):
    return ''.join(input_string.split())

if __name__ == '__main__':
    sample_input = "  This is   a \n\t sample string with \t various \t whitespace.  "
    result = minify_text(sample_input)
    print(result)