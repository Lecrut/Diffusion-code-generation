def strip_whitespace(strings):
    return list(map(str.strip, strings))

if __name__ == '__main__':
    sample_strings = ["  hello  ", "world  ", "  python", " foo bar "]
    result = strip_whitespace(sample_strings)
    print(result)