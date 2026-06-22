def strip_whitespace_list(strings):
    return list(map(str.strip, strings))

if __name__ == '__main__':
    sample_data = ["  hello  ", "  world  ", "  test  ", "  data  "]
    result = strip_whitespace_list(sample_data)
    print(result)