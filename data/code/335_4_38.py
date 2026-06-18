class WordSplitter:
    def split(self, text):
        return [word for word in text.split() if word]
if __name__ == '__main__':
    splitter = WordSplitter()
    sample_text = "  Hello   World\nThis is a test."
    result = splitter.split(sample_text)
    print(result)