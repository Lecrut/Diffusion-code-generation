def remove_spaces(input_string):
    WHITESPACE_TYPES = (" ", "\t", "\n", "\r")
    result = input_string
    for whitespace in WHITESPACE_TYPES:
        result = result.replace(whitespace, "")
    return result

if __name__ == '__main__':
    sample_input = "This is a \tsample string.\nIt contains various types of spaces."
    result = remove_spaces(sample_input)
    print(result)