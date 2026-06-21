import re

class WhitespaceProcessor:
    WHITESPACE_PATTERN = re.compile(r'\s+')

    @staticmethod
    def remove_whitespace(input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        return WhitespaceProcessor.WHITESPACE_PATTERN.sub('', input_string)

if __name__ == '__main__':
    sample_input = "  This is a   test string with \t various \n whitespace characters.  "
    processor = WhitespaceProcessor()
    result = processor.remove_whitespace(sample_input)
    print(result)