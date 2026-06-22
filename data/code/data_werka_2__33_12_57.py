def remove_whitespace(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    return ''.join(input_string.split())

if __name__ == '__main__':
    sample_input = "  This is a   unique test string with \t various \n whitespace characters.  "
    result = remove_whitespace(sample_input)
    print(result)