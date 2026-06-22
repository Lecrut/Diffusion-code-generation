def validate_input(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")

def remove_spaces(input_string):
    validate_input(input_string)
    return input_string.replace(' ', '')

if __name__ == '__main__':
    sample_input = "  This is   a test string with  spaces  "
    result = remove_spaces(sample_input)
    print(result)