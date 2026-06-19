def filter_alphanumeric(input_string):
    result = ''.join(char for char in input_string if char.isalnum())
    return result

if __name__ == '__main__':
    sample_input = "Hello, World! 123"
    filtered_output = filter_alphanumeric(sample_input)
    print(filtered_output)