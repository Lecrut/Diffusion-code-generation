def is_valid_string(input_value):
    return isinstance(input_value, str)

def remove_whitespace(input_string):
    if not is_valid_string(input_string):
        raise ValueError("Input must be a string")
    return ''.join(input_string.split())

if __name__ == '__main__':
    sample_input = "  This is another   test string with \t various \n whitespace characters.  "
    try:
        result = remove_whitespace(sample_input)
        print(result)
    except ValueError as e:
        print(e)