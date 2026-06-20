def replace_whitespace_with_underscores(text):
    return ''.join('_' if c.isspace() else c for c in text)

if __name__ == '__main__':
    sample1 = "hello world"
    sample2 = "  leading and trailing  "
    sample3 = "tabs\there\nand newlines"
    print(replace_whitespace_with_underscores(sample1))
    print(replace_whitespace_with_underscores(sample2))
    print(replace_whitespace_with_underscores(sample3))