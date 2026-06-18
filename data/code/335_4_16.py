class StringSplitter:
    def split_whitespace(self, text):
        return [word for word in text.split() if len(word) > 0]
if __name__ == '__main__':
    splitter = StringSplitter()
    sample_text = "Hello   world\nPython\tcode"
    result = splitter.split_whitespace(sample_text)
    print(result)