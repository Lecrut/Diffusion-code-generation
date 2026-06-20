def strip_whitespace(text):
    return text.strip()

if __name__ == '__main__':
    sample_string = '  hello world  '
    result = strip_whitespace(sample_string)
    print(repr(result))