def strip_strings(strings):
    return list(map(str.strip, strings))

if __name__ == '__main__':
    sample_data = ['  hello  ', '\tworld\n', '  python  ', '\n  code  ', '  ']
    result = strip_strings(sample_data)
    print(result)