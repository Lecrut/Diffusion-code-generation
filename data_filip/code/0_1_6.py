def extract_numeric_string(s):
    return ''.join([char for char in s if char.isdigit()])

if __name__ == '__main__':
    sample_string = "Hello 123 World 456!"
    result = extract_numeric_string(sample_string)
    print(result)