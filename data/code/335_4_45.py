class StringSplitter:
    def split(self, text):
        return [token for token in text.split() if len(token) > 0]
if __name__ == '__main__':
    splitter = StringSplitter()
    sample_text = "Hello   world\nThis is\t a test."
    result = splitter.split(sample_text)
    print(result)