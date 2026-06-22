import string

def is_valid_input(input_string):
    return isinstance(input_string, str)

def remove_all_spaces(input_string):
    if not is_valid_input(input_string):
        raise ValueError('Input must be a string')
    return input_string.translate(str.maketrans('', '', string.whitespace))
if __name__ == '__main__':
    sample_input = 'This is a \tsample string.\nIt contains various whitespace characters.'
    result = remove_all_spaces(sample_input)
    print(result)