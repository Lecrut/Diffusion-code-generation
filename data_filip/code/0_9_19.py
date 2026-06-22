def extract_digits(mixed_string):
    return ''.join(char for char in mixed_string if char.isdigit())

if __name__ == '__main__':
    sample = "abc123def456"
    print(extract_digits(sample))