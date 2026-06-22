def extract_numbers(input_string):
    return ''.join([char for char in input_string if char.isdigit()])

if __name__ == '__main__':
    sample_input = "abc123xyz456"
    result = extract_numbers(sample_input)
    print(result)