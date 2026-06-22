def remove_whitespace(input_string):
    if not isinstance(input_string, str):
        raise ValueError('Input must be a string')
    return ''.join(input_string.split())
if __name__ == '__main__':
    sample_input = '  Here is another example with \t different \n whitespace.  '
    try:
        cleaned_string = remove_whitespace(sample_input)
        print(cleaned_string)
    except ValueError as e:
        print(e)