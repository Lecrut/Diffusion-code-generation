def remove_spaces(input_string):
    return input_string.replace(' ', '').replace('\t', '').replace('\n', '').replace('\r', '')

if __name__ == '__main__':
    sample_input = "This is a \tsample string.\nIt contains multiple\ttypes of whitespace."
    result = remove_spaces(sample_input)
    print(result)