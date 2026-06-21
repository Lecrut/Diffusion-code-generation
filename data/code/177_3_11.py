class StringSplitter:
    def split(self, input_string):
        return input_string.split(' ')

if __name__ == '__main__':
    splitter = StringSplitter()
    result1 = splitter.split("this is a sample string")
    result2 = splitter.split("another string to split")
    print(result1)
    print(result2)