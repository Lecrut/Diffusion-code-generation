def replace_whitespace_with_underscores(s):
    return ''.join('_' if c.isspace() else c for c in s)

if __name__ == '__main__':
    sample = "hello world   this\nis a\ttest"
    print(replace_whitespace_with_underscores(sample))