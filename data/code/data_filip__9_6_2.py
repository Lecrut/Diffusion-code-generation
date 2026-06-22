def strip_whitespace_from_list(strings):
    return list(map(str.strip, strings))

if __name__ == '__main__':
    sample = ['  hello  ', ' world ', '\ttest\n', '  no change  ']
    result = strip_whitespace_from_list(sample)
    print(result)