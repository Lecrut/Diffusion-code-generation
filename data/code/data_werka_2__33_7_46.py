def is_valid_input(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")

def remove_all_spaces(input_string):
    is_valid_input(input_string)
    return ''.join(char for char in input_string if not char.isspace())

if __name__ == '__main__':
    sample_input = "  This is an example with \t various whitespace characters.\n"
    result = remove_all_spaces(sample_input)
    print(result)