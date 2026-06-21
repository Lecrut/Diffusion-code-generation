def remove_spaces(input_string):
    whitespace_map = {
        ' ': '',
        '\t': '',
        '\n': '',
        '\r': ''
    }
    for ws, replacement in whitespace_map.items():
        input_string = input_string.replace(ws, replacement)
    return input_string

if __name__ == '__main__':
    sample_input = "This is a \tsample string.\nIt contains various types of spaces."
    result = remove_spaces(sample_input)
    print(result)