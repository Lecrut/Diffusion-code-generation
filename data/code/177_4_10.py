class TextSplitter:
    def split_by_whitespace(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        return text.split()

if __name__ == '__main__':
    splitter = TextSplitter()
    sample_text = "Hello World This is a test"
    result = splitter.split_by_whitespace(sample_text)
    print(result)