class TextSplitter:
    def split_text(self, text):
        return text.split()

if __name__ == '__main__':
    splitter = TextSplitter()
    sample_string = "This is a sample sentence for splitting by whitespace"
    result = splitter.split_text(sample_string)
    print(result)