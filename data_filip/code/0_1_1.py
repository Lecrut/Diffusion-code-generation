def extract_numeric_string(s):
    return ''.join([c for c in s if c.isdigit()])

if __name__ == '__main__':
    sample = "abc123def456ghi789"
    print(extract_numeric_string(sample))