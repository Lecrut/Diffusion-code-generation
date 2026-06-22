import re

class TextProcessor:
    def __init__(self):
        self.whitespace_pattern = re.compile(r'\s+')

    def remove_whitespace(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        return self.whitespace_pattern.sub('', input_string)

if __name__ == '__main__':
    sample_input_1 = "  This is a   test string with \t various \n whitespace characters.  "
    sample_input_2 = "Another\texample\nwith different\twhitespace."

    processor = TextProcessor()

    result_1 = processor.remove_whitespace(sample_input_1)
    result_2 = processor.remove_whitespace(sample_input_2)

    print("Result for sample_input_1:", result_1)
    print("Result for sample_input_2:", result_2)