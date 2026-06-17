class StringSplitter:
    def split(self, text):
        return [word for word in text.split() if word]
if __name__ == '__main__':
    splitter = StringSplitter()
    sample_text = "  Hello   world\n\tPython \tcode"
    result = splitter.split(sample_text)
    print(result)