def strip_whitespace(text):
    return text.strip()
if __name__ == '__main__':
    sample_values = ['  hello world  ', '\t\npython code\t\n', '   spaces   everywhere   ', 'no_whitespace_here', '', '   ']
    for value in sample_values:
        result = strip_whitespace(value)
        print(repr(result))