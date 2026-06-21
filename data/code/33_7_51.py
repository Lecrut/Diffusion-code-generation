def remove_all_spaces(input_string):
    whitespace_mapping = {char: '' for char in ' \t\n\r\x0b\x0c'}
    return ''.join(whitespace_mapping.get(char, char) for char in input_string)

if __name__ == '__main__':
    sample_input = "This is a \tsample string.\nIt contains various whitespace characters."
    result = remove_all_spaces(sample_input)
    print(result)