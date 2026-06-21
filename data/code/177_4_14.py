class TextSplitter:
    def split(self, text):
        return text.split()

if __name__ == '__main__':
    splitter = TextSplitter()
    sample_string = "This is a sample sentence for splitting by whitespace"
    result = splitter.split(sample_string)
    print(result)