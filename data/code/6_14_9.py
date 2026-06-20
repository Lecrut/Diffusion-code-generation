def replace_spaces_with_underscores(text):
    return text.replace(' ', '_')
if __name__ == '__main__':
    sample_strings = ['hello world', 'foo bar baz', 'no spaces here', '  leading and trailing  ', 'multiple   spaces   between', '', ' ']
    for s in sample_strings:
        print(replace_spaces_with_underscores(s))