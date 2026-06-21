def remove_spaces(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    whitespace_types = [" ", "\t", "\n", "\r"]
    result = input_string
    for ws in whitespace_types:
        result = result.replace(ws, "")
    
    return result

if __name__ == '__main__':
    sample_input = "This is a \tsample string.\nIt contains various types of spaces."
    try:
        result = remove_spaces(sample_input)
        print(result)
    except ValueError as e:
        print(e)