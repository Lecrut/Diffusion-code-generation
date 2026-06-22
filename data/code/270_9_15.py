def remove_spaces(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    return ''.join(char for char in input_string if char != ' ')

if __name__ == '__main__':
    sample_input = "Hello World"
    print(remove_spaces(sample_input))