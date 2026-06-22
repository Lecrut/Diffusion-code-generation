def trim_whitespace_sequence(strings):
    return [s.strip() for s in strings]

if __name__ == '__main__':
    sample_data = ["  hello  ", "\tworld\n", "  python  ", "code  ", "  test  "]
    result = trim_whitespace_sequence(sample_data)
    print(result)