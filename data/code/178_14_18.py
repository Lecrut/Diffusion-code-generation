import re

class StringSplitter:
    WHITESPACE_PATTERN = r'\s+'
    
    @staticmethod
    def split_string(text):
        words = re.split(StringSplitter.WHITESPACE_PATTERN, text)
        return [word for word in words if word]

if __name__ == '__main__':
    sample_string = "  Hello   world! How are you? "
    splitter = StringSplitter()
    result = splitter.split_string(sample_string)
    print(result)