class StringSplitter:
    @staticmethod
    def split_by_spaces(input_string):
        return input_string.split()

if __name__ == '__main__':
    sample_string = 'Hello World from Python'
    result = StringSplitter.split_by_spaces(sample_string)
    print(result)