class StringSplitter:
    def split(self, text):
        return [word for word in text.split() if word]
if __name__ == '__main__':
    splitter = StringSplitter()
    sample_text = "  hello   world\n\ttest\r"
    result = splitter.split(sample_text)
    print(result)