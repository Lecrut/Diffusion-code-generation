class StringSplitter:
    WHITESPACE_PATTERN = r'\s+'

    @staticmethod
    def split_string(text):
        return re.split(StringSplitter.WHITESPACE_PATTERN, text)

if __name__ == '__main__':
    splitter = StringSplitter()
    sample1 = "data analysis with python"
    result1 = splitter.split_string(sample1)
    print(f"Input: '{sample1}'")
    print(f"Output: {result1}")