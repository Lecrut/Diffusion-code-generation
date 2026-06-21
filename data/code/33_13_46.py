def remove_spaces(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    whitespace_types = [" ", "\t", "\n"]
    result = input_string
    for ws in whitespace_types:
        result = result.replace(ws, "")
    return result

if __name__ == '__main__':
    sample_input = "This is a \tsample string.\nIt contains spaces, tabs,\tand newlines."
    result = remove_spaces(sample_input)
    print(result)