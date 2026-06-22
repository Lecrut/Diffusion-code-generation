import re

def is_valid_string(input_value):
    return isinstance(input_value, str)

def remove_whitespace(input_string):
    if not is_valid_string(input_string):
        raise ValueError('Input must be a string')

    def core_remove_whitespace(s):
        pattern = re.compile('\\s+')
        return pattern.sub('', s)
    return core_remove_whitespace(input_string)
if __name__ == '__main__':
    sample_input = '  This is a   test string with \t various \n whitespace characters.  '
    result = remove_whitespace(sample_input)
    print(result)