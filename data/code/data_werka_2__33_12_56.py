def remove_whitespace(input_string):
    if not isinstance(input_string, str):
        raise ValueError('Input must be a string')
    cleaned_string = ''.join(input_string.split())
    return cleaned_string
if __name__ == '__main__':
    sample_input = '  Another example with \t different \n whitespace.  '
    try:
        result = remove_whitespace(sample_input)
        print(result)
    except ValueError as e:
        print(e)