def remove_all_spaces(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    return ''.join(char for char in input_string if not char.isspace())

if __name__ == '__main__':
    sample_input = "This is a \tsample string.\nIt contains various whitespace characters."
    result = remove_all_spaces(sample_input)
    print(result)