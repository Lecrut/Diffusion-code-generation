def extract_digits(mixed_string):
    return [int(char) for char in mixed_string if char.isdigit()]

if __name__ == '__main__':
    sample_data = "abc123def45g6"
    print(extract_digits(sample_data))