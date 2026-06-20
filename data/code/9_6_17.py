def strip_whitespace_strings(strings):
    return list(map(str.strip, strings))

if __name__ == '__main__':
    sample_data = ["  hello  ", "\tworld\n", "  python  ", "  test  ", "  data  "]
    result = strip_whitespace_strings(sample_data)
    print(result)