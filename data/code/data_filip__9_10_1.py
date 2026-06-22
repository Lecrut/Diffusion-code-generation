def strip_whitespace(input_string):
    return input_string.strip()
if __name__ == '__main__':
    sample_strings = ['  hello world  ', '\t\nHello, World!\n\t', '   no whitespace here   ', '   spaces   and   tabs\t\n', '', '   ', 'no leading or trailing spaces']
    for s in sample_strings:
        result = strip_whitespace(s)
        print(result)