def filter_and_join_numeric_chars(s):
    return ''.join([c for c in s if c.isdigit()])

if __name__ == '__main__':
    sample_string = "abc123def456ghi789"
    result = filter_and_join_numeric_chars(sample_string)
    print(result)