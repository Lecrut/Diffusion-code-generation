def filter_digits(s):
    return [int(c) for c in s if c.isdigit()]

if __name__ == '__main__':
    sample = "abc123def456"
    print(filter_digits(sample))