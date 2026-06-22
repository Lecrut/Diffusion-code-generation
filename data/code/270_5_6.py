import re

class StringProcessor:
    def remove_spaces(self, input_string):
        return re.sub(r'\s+', '', input_string)

if __name__ == '__main__':
    processor = StringProcessor()
    sample_strings = ["hello world", "  multiple spaces here  ", "singleword", "a b c"]
    for s in sample_strings:
        print(processor.remove_spaces(s))