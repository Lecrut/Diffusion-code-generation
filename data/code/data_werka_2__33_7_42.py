def remove_all_spaces(input_string):
    WHITESPACE_CHARS = " \t\n\r\v\f"
    return ''.join(char for char in input_string if char not in WHITESPACE_CHARS)

if __name__ == '__main__':
    sample_input = "This is a \tsample string.\nIt contains various whitespace characters."
    result = remove_all_spaces(sample_input)
    print(result)