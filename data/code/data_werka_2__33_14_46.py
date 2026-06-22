def remove_spaces(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    return input_string.replace(' ', '')

if __name__ == '__main__':
    sample_input = "  This is   a test string with multiple spaces.  "
    try:
        result = remove_spaces(sample_input)
        print(result)
    except ValueError as e:
        print(e)