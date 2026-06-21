import re
WHITESPACE_PATTERN = '\\s+'

def remove_whitespace(input_string):
    if not isinstance(input_string, str):
        raise ValueError('Input must be a string')
    return re.sub(WHITESPACE_PATTERN, '', input_string)

class TextProcessor:

    def __init__(self):
        self.whitespace_pattern = re.compile(WHITESPACE_PATTERN)

    def process_text(self, text):
        return self.whitespace_pattern.sub('', text)
if __name__ == '__main__':
    sample_input = '  This is a   test string with \t various \n whitespace characters.  '
    result_function = remove_whitespace(sample_input)
    print('Function Result:', result_function)
    processor = TextProcessor()
    result_class = processor.process_text(sample_input)
    print('Class Result:', result_class)