class StringSplitter:
    def split(self, text):
        return [word for word in text.split() if len(word)]
if __name__ == '__main__':
    splitter = StringSplitter()
    sample_text = "  hello world   python\n\tcode is fun"
    result = splitter.split(sample_text)
    print(result)