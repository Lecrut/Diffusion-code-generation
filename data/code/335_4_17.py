class StringSplitter:
    def split(self, s):
        return [word for word in s.split() if len(word) > 0]
if __name__ == '__main__':
    splitter = StringSplitter()
    text = "Hello   world\nthis is\t a test"
    result = splitter.split(text)
    print(result)