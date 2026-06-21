class StringSplitter:
    def __init__(self, input_string):
        self.input_string = input_string

    def split_by_spaces(self):
        return self.input_string.split()

if __name__ == '__main__':
    splitter = StringSplitter('Hello World from Python')
    result = splitter.split_by_spaces()
    print(result)