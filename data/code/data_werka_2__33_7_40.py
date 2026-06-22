def remove_all_spaces(input_string):
    if not input_string:
        return ""
    
    result = []
    for char in input_string:
        if not char.isspace():
            result.append(char)
    
    return ''.join(result)

if __name__ == '__main__':
    sample_input = "This is a \tsample string.\nIt contains various whitespace characters."
    result = remove_all_spaces(sample_input)
    print(result)