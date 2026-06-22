def strip_whitespace(string_list):
    return list(map(str.strip, string_list))

if __name__ == '__main__':
    sample_data = ["  hello  ", "  world  ", "  python  "]
    result = strip_whitespace(sample_data)
    print(result)