class StringSplitter:
    def split(self, s):
        return [word for word in s.split() if len(word) > 0]
if __name__ == '__main__':
    splitter = StringSplitter()
    sample_input = "Hello   world\nPython\tcode"
    result = splitter.split(sample_input)
    print(result)