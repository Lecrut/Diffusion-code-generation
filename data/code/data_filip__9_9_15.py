def strip_whitespace_from_tuple(strings):
    return tuple(s.strip() for s in strings)

if __name__ == '__main__':
    sample_data = ("  hello  ", " world ", "\ttest\n", "  python  ")
    result = strip_whitespace_from_tuple(sample_data)
    print(result)