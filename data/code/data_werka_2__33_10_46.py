import re

def remove_whitespace(input_string):
    if not isinstance(input_string, str):
        raise ValueError('Input must be a string')
    whitespace_map = {char: '' for char in ' \t\n\r\x0c\x0b'}
    return re.sub('\\s+', '', input_string, flags=re.UNICODE)
if __name__ == '__main__':
    sample_input = '  This is a   test string with \t various \n whitespace characters.  '
    result = remove_whitespace(sample_input)
    print(result)