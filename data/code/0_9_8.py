def extract_digits(mixed_string):
    return ''.join(d for d in mixed_string if d.isdigit())

if __name__ == '__main__':
    sample = "abc123def456ghi789"
    result = extract_digits(sample)
    print(result)