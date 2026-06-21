def remove_whitespace(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    def is_whitespace(char):
        return char.isspace()
    
    filtered_chars = (char for char in input_string if not is_whitespace(char))
    return ''.join(filtered_chars)

if __name__ == '__main__':
    sample_input = "  This is a   test string with \t various \n whitespace characters.  "
    try:
        result = remove_whitespace(sample_input)
        print(result)
    except ValueError as e:
        print(e)