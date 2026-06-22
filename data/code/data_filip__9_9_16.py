def strip_whitespace_from_tuple(strings):
    return tuple(s.strip() for s in strings)

if __name__ == '__main__':
    sample = ('  hello  ', '\tworld\n', '  foo  bar  ', '    ')
    result = strip_whitespace_from_tuple(sample)
    print(result)