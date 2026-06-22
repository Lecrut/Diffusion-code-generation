def extract_numeric_string(s):
    return ''.join([c for c in s if c.isdigit()])

if __name__ == '__main__':
    sample_string = "abc123def45ghi67"
    result = extract_numeric_string(sample_string)
    print(result)