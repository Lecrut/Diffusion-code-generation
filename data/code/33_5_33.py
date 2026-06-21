def non_whitespace_generator(input_string):
    return (char for char in input_string if not char.isspace())

if __name__ == '__main__':
    sample_input = "Hello, World! This is a test."
    result = ''.join(non_whitespace_generator(sample_input))
    print(result)