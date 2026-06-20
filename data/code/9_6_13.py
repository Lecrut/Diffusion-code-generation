def strip_whitespace(strings_list):
    return list(map(str.strip, strings_list))

if __name__ == '__main__':
    sample_data = ["  hello  ", "world  ", "  foo bar  ", "baz"]
    result = strip_whitespace(sample_data)
    print(result)