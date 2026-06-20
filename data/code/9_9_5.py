def strip_whitespace_from_tuple(strings_tuple):
    return tuple(s.strip() for s in strings_tuple)

if __name__ == '__main__':
    sample_input = ("  hello  ", "  world  ", "python  ", "  test  ")
    result = strip_whitespace_from_tuple(sample_input)
    print(result)