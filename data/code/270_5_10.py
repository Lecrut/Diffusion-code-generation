import re

class StringProcessor:
    def remove_spaces(self, input_string):
        return re.sub(r'\s+', '', input_string)

if __name__ == '__main__':
    processor = StringProcessor()
    sample_input1 = "hello world"
    sample_input2 = "  multiple spaces here  "
    print(processor.remove_spaces(sample_input1))
    print(processor.remove_spaces(sample_input2))