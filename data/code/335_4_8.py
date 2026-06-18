class StringSplitter:
    def split(self, s):
        return [word for word in s.split() if len(word) > 0]
if __name__ == '__main__':
    splitter = StringSplitter()
    test_string = "Hello   world\n\tPython"
    result = splitter.split(test_string)
    print(result)