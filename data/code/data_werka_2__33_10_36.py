import re

class StringProcessor:
    WHITESPACE_PATTERN = re.compile(r'\s+')

    @staticmethod
    def remove_whitespace(input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        return StringProcessor.WHITESPACE_PATTERN.sub('', input_string)

if __name__ == '__main__':
    sample_input = "  This is another   example string with \t various \n whitespace characters.  "
    result = StringProcessor.remove_whitespace(sample_input)
    print(result)