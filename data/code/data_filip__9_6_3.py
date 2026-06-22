def strip_whitespace_list(string_list):
    return list(map(str.strip, string_list))

if __name__ == '__main__':
    sample_data = ["  hello  ", "\tworld\n", "  Python  ", "  code  ", "  test  "]
    result = strip_whitespace_list(sample_data)
    print(result)