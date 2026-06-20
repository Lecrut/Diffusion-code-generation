def extract_digits(input_string):
    return ''.join(char for char in input_string if char.isdigit())

if __name__ == '__main__':
    sample_text = "abc123def456"
    result = extract_digits(sample_text)
    print(result)