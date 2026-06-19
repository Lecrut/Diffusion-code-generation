def filter_alphanumeric(input_string):
    return ''.join(char for char in input_string if char.isalnum())

if __name__ == '__main__':
    sample_input = "Hello, World! 123"
    result = filter_alphanumeric(sample_input)
    print(result)