import re

class StringSplitter:
    def split_string(self, text):
        return re.split(r'\s+', text)

if __name__ == '__main__':
    splitter = StringSplitter()
    input_string = "  This   is a test string with multiple spaces "
    result = splitter.split_string(input_string)
    print(result)