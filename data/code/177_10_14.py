import re

class StringSplitter:
    WHITESPACE_PATTERN = r'\s+'

    @staticmethod
    def split_string(text):
        return re.split(StringSplitter.WHITESPACE_PATTERN, text)

if __name__ == '__main__':
    input_string = "  This   is a test string with multiple spaces "
    result = StringSplitter.split_string(input_string)
    print(result)