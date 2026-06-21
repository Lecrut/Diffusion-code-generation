import re

def remove_whitespace(input_string):

    def compile_whitespace_pattern():
        return re.compile('\\s+')
    whitespace_pattern = compile_whitespace_pattern()
    cleaned_string = whitespace_pattern.sub('', input_string)
    return cleaned_string
if __name__ == '__main__':
    sample_input = 'Another example with \t different \n types of whitespace.'
    result = remove_whitespace(sample_input)
    print(result)