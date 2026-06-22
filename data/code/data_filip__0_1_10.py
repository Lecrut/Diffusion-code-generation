def extract_numeric_string(s):
    return ''.join([c for c in s if c.isdigit()])

if __name__ == '__main__':
    sample = "a1b2c3!@#456"
    result = extract_numeric_string(sample)
    print(result)