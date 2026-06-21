class StringSplitter:
    def split_by_spaces(self, input_string):
        return input_string.split()

if __name__ == '__main__':
    splitter = StringSplitter()
    sample_string = 'Hello World from Python'
    result = splitter.split_by_spaces(sample_string)
    print(result)