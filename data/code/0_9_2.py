def extract_digits(text):
    return ''.join(char for char in text if char.isdigit())

if __name__ == '__main__':
    sample_string = "abc123def456ghi789"
    result = extract_digits(sample_string)
    print(result)