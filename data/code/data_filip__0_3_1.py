def extract_digits(input_string):
    return ''.join(char for char in input_string if char.isdigit())

if __name__ == '__main__':
    sample_input = "Hello123World456"
    result = extract_digits(sample_input)
    print(result)