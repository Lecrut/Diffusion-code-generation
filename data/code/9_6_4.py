def strip_whitespace_from_list(strings):
    return list(map(str.strip, strings))

if __name__ == '__main__':
    sample_list = ['  hello  ', '\tworld\n', '  python  ', '   code  ', ' test ']
    result = strip_whitespace_from_list(sample_list)
    print(result)