class StringSplitter:
    def split(self, s):
        return [word for word in s.split() if word]
if __name__ == '__main__':
    splitter = StringSplitter()
    test_string = "  hello   world\n\ttest\r"
    result = splitter.split(test_string)
    print(result)