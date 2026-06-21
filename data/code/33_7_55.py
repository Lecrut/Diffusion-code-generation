def remove_all_spaces(input_string):
    whitespace_map = {ord(c): None for c in ' \t\n\r\x0b\x0c'}
    return input_string.translate(whitespace_map)

if __name__ == '__main__':
    sample_input = "This is a \tsample string.\nIt contains various whitespace characters."
    result = remove_all_spaces(sample_input)
    print(result)