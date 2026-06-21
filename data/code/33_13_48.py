def remove_spaces(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    whitespace_types = [" ", "\t", "\n", "\r"]
    for ws in whitespace_types:
        input_string = input_string.replace(ws, "")
    
    return input_string

if __name__ == '__main__':
    sample_input = "This is a \tsample string.\nIt contains various types of spaces."
    result = remove_spaces(sample_input)
    print(result)