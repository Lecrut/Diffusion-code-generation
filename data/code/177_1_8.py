class StringSplitter:
    @staticmethod
    def split_string(input_string):
        return input_string.split()

if __name__ == '__main__':
    splitter = StringSplitter()
    sample_string = 'Hello World from Python'
    result = splitter.split_string(sample_string)
    print(result)