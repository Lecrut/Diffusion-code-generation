class StringSplitter:
    def split_whitespace(self, text):
        return [word for word in text.split() if len(word) > 0]
if __name__ == '__main__':
    splitter = StringSplitter()
    sample_text = "Hello   world\nthis is\t a test"
    result = splitter.split_whitespace(sample_text)
    print(result)