def extract_numeric_string(s):
    return "".join([char for char in s if char.isdigit()])

if __name__ == '__main__':
    sample_input = "abc123def456!@#789xyz"
    result = extract_numeric_string(sample_input)
    print(result)