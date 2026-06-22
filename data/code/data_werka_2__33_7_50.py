def remove_all_spaces(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    def is_whitespace(char):
        return char.isspace()
    
    return ''.join(filter(lambda x: not is_whitespace(x), input_string))

if __name__ == '__main__':
    sample_input = "This is a \tsample string.\nIt contains various whitespace characters."
    result = remove_all_spaces(sample_input)
    print(result)