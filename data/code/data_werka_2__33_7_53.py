import re

class StringProcessor:
    def __init__(self, input_string):
        self.input_string = input_string

    def remove_all_spaces(self):
        return re.sub(r'\s+', '', self.input_string)

if __name__ == '__main__':
    sample_input1 = "This is a \tsample string.\nIt contains various whitespace characters."
    processor1 = StringProcessor(sample_input1)
    result1 = processor1.remove_all_spaces()
    print(result1)

    sample_input2 = "  This is another\texample with\nmultiple spaces.  "
    processor2 = StringProcessor(sample_input2)
    result2 = processor2.remove_all_spaces()
    print(result2)