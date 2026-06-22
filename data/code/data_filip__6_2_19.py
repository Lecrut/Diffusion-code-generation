def replace_whitespace(s):
    return ''.join('_' if c.isspace() else c for c in s)

if __name__ == '__main__':
    result = replace_whitespace('hello world')
    print(result)