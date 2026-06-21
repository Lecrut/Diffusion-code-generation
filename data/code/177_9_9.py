class StringSplitter:
    def split_by_whitespace(self, text):
        return text.split()

if __name__ == '__main__':
    splitter = StringSplitter()
    sample1 = "data analysis with python"
    result1 = splitter.split_by_whitespace(sample1)
    print(f"Input: '{sample1}'")
    print(f"Output: {result1}")