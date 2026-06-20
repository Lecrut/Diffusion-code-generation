def extract_digits_from_string(input_string):
    digits = (char for char in input_string if char.isdigit())
    return "".join(digits)

if __name__ == '__main__':
    sample_string = "abc123xyz456"
    result = extract_digits_from_string(sample_string)
    print(result)