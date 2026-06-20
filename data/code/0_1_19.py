def extract_numbers(s):
    return ''.join([c for c in s if c.isdigit()])

if __name__ == '__main__':
    sample_string = "abc123def456ghi789"
    result = extract_numbers(sample_string)
    print(result)