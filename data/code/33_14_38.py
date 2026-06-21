def remove_spaces(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    return ''.join(input_string.split())

if __name__ == '__main__':
    sample_input = "  This is   an example string with spaces.  "
    result = remove_spaces(sample_input)
    print(result)