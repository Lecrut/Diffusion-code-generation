def replace_whitespace_with_underscores(text):
    return ''.join('_' if c.isspace() else c for c in text)

if __name__ == '__main__':
    print(replace_whitespace_with_underscores('hello world'))
    print(replace_whitespace_with_underscores('foo\tbar\nbaz'))
    print(replace_whitespace_with_underscores('no_whitespace_here'))