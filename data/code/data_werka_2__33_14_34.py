def remove_spaces(input_string):
    if not isinstance(input_string, str):
        raise ValueError('Input must be a string')
    if input_string == '':
        return ''
    return ''.join(input_string.split())
if __name__ == '__main__':
    sample_input = '  This is   a test string with  spaces  '
    result = remove_spaces(sample_input)
    print(result)