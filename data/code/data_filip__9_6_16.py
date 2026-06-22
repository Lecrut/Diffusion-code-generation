def strip_whitespace_list(strings):
    stripped = map(str.strip, strings)
    return list(stripped)

if __name__ == '__main__':
    sample_list = ['  hello  ', '  world  ', '  python  ', '  performance  ', '  testing  ']
    result = strip_whitespace_list(sample_list)
    print(result)