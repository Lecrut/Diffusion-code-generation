def replace_whitespace_with_underscores(text):
    return text.replace(' ', '_').replace('\t', '_').replace('\n', '_').replace('\r', '_').replace('\x0b', '_').replace('\x0c', '_')

if __name__ == '__main__':
    print(replace_whitespace_with_underscores("Hello World!\nThis is a\ttest."))