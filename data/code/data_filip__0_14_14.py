def filter_digits(s):
    return [int(c) for c in s if c.isdigit()]

if __name__ == '__main__':
    result = filter_digits("abc123def456")
    print(result)