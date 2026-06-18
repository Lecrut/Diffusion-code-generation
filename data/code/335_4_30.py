class StringSplitter:
    def split(self, text):
        return [word for word in text.split() if len(word) > 0]
if __name__ == '__main__':
    splitter = StringSplitter()
    test_string = "Hello   world\n\tPython"
    result = splitter.split(test_string)
    print(result)