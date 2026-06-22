import re

class StringProcessor:
    @staticmethod
    def remove_spaces(input_string):
        return re.sub(r'\s+', '', input_string)

if __name__ == '__main__':
    sample_input = "Hello, World! This is a test."
    processor = StringProcessor()
    result = processor.remove_spaces(sample_input)
    print(result)