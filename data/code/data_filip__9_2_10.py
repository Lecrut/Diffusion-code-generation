def trim_whitespace(strings):
    return [s.strip() for s in strings]

if __name__ == '__main__':
    sample_data = ["  hello  ", "world  ", "  python "]
    result = trim_whitespace(sample_data)
    print(result)