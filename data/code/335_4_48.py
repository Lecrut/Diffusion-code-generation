class StringSplitter:
    def split(self, text):
        return [word for word in text.split() if len(word) > 0]
if __name__ == '__main__':
    splitter = StringSplitter()
    sample_text = "Hello   world\nThis is\t a test string."
    result = splitter.split(sample_text)
    print(result)