def extract_digits(input_string):
    return ''.join([char for char in input_string if char.isdigit()])

if __name__ == '__main__':
    sample_string = "abc123def456ghi789"
    result = extract_digits(sample_string)
    print(result)