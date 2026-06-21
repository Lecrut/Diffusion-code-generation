import re

def is_valid_string(input_string):
    return isinstance(input_string, str)

def remove_whitespace(input_string):
    if not is_valid_string(input_string):
        raise ValueError("Input must be a string")
    return re.sub(r'\s+', '', input_string)

class StringProcessor:
    def __init__(self, input_string):
        if not is_valid_string(input_string):
            raise ValueError("Input must be a string")
        self.input_string = input_string

    def process(self):
        return remove_whitespace(self.input_string)

if __name__ == '__main__':
    sample_input = "  This is another   test with \t different \n whitespace. "
    processor = StringProcessor(sample_input)
    result = processor.process()
    print(result)