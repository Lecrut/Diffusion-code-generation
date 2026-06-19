def remove_spaces(input_string):
    return input_string.replace(' ', '').replace('\t', '').replace('\n', '').replace('\r', '')

if __name__ == '__main__':
    sample_string = "This is a \tsample string.\nIt contains multiple\ttypes of whitespace."
    result = remove_spaces(sample_string)
    print(result)